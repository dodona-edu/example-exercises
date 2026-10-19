#!/bin/sh
# Usage: check-examples.sh <language>   run every TESTed example that has a reference solution in <language>
#        check-examples.sh --languages  print the languages to check as a JSON list
# Needs python3 and the TESTed source at $JUDGE (default /judge), as in the dodona-tested image.
# The TESTed CLI ignores evaluation.options of the exercise config (linter, mode, eslint_config, ...).

JUDGE=${JUDGE:-/judge}

# Exercise/language pairs that must fail until fixed; they fail the check once they pass.
# smallest/haskell: TESTed generates `smallest 5 :: Int 6 :: Int`, https://github.com/dodona-edu/universal-judge/issues/568
expected_failure() {
  case $1 in
    smallest/haskell) return 0 ;;
  esac
  return 1
}

# Per exercise (a directory under tested/ with a config.json): <exercise>\t<suite>\t<solution or empty>.
LIST='
import json, os, sys

EXTENSIONS = {
    "py": "python", "sh": "bash", "c": "c", "cpp": "cpp", "cs": "csharp",
    "hs": "haskell", "java": "java", "js": "javascript", "kt": "kotlin", "ts": "typescript",
}
tested, language = sys.argv[1], sys.argv[2]


def read(path):
    with open(path) as file:
        return json.load(file)


def merge(parent, child):
    merged = dict(parent)
    for key, value in child.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def solutions(exercise):
    found = {}
    folder = os.path.join(exercise, "solution")
    for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        extension = name.rsplit(".", 1)[-1]
        if extension in EXTENSIONS:
            found.setdefault(EXTENSIONS[extension], "solution/" + name)
    return found


exercises = []


def walk(directory, inherited):
    config_path = os.path.join(directory, "config.json")
    if os.path.isfile(config_path):
        config = merge(inherited, read(config_path))
        exercises.append((
            os.path.relpath(directory, tested),
            config.get("evaluation", {}).get("test_suite", "suite.yaml"),
            config.get("programming_language"),
            solutions(directory),
        ))
        return
    dirconfig = os.path.join(directory, "dirconfig.json")
    if os.path.isfile(dirconfig):
        inherited = merge(inherited, read(dirconfig))
    for name in sorted(os.listdir(directory)):
        if os.path.isdir(os.path.join(directory, name)):
            walk(os.path.join(directory, name), inherited)


walk(tested, {})
if language == "--languages":
    languages = set()
    for _, _, configured, found in exercises:
        languages.update(found)
        if configured:
            languages.add(configured)
    print(json.dumps(sorted(languages)))
else:
    for exercise, suite, configured, found in exercises:
        if language in found:
            print("%s\t%s\t%s" % (exercise, suite, found[language]))
        elif configured == language:
            print("%s\t%s\t" % (exercise, suite))
'

# Pass = at least one close-test and every close-test is correct; prints the others.
CHECK='
import json, sys
tests, expected = [], None
for line in open(sys.argv[1]):
    if not line.startswith("{"):
        continue
    update = json.loads(line)
    if update.get("command") == "start-test":
        expected = update.get("expected")
    elif update.get("command") == "close-test":
        tests.append((expected, update.get("generated"), update["status"]["enum"]))
bad = [t for t in tests if t[2] != "correct"]
for expected, generated, status in bad:
    print("  %s: expected %r, generated %r" % (status, expected, generated))
if not tests:
    print("  no tests were run")
sys.exit(1 if bad or not tests else 0)
'

root=$(cd "$(dirname "$0")/.." && pwd)

if [ "$1" = "--languages" ]; then
  python3 -c "$LIST" "$root/tested" --languages
  exit $?
fi

language=$1
case $language in
  ""|*[!a-z]*) echo "usage: $0 <language> | --languages" >&2; exit 2 ;;
esac

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
python3 -c "$LIST" "$root/tested" "$language" > "$tmp/list" || exit 1
exit_code=0
tab=$(printf '\t')

while IFS=$tab read -r exercise suite solution; do
  if [ -z "$solution" ]; then
    echo "FAIL $exercise ($language): no reference solution"
    exit_code=1
    continue
  fi

  rm -rf "$tmp/exercise"
  cp -R "$root/tested/$exercise" "$tmp/exercise"
  out="$tmp/out"
  details="$tmp/details"
  : > "$details"
  if [ ! -f "$tmp/exercise/evaluation/$suite" ]; then
    echo "test suite evaluation/$suite does not exist" > "$out"
    passed=false
  elif (cd "$JUDGE" && python3 -m tested.cli -e "$tmp/exercise" -p "$language" \
        -s "$tmp/exercise/$solution" -t "$tmp/exercise/evaluation/$suite" -f) < /dev/null > "$out" 2>&1 \
     && python3 -c "$CHECK" "$out" > "$details"; then
    passed=true
  else
    passed=false
  fi

  if $passed && expected_failure "$exercise/$language"; then
    echo "UNEXPECTED PASS $exercise ($language): remove \"$exercise/$language\" from expected_failure in .github/check-examples.sh"
    exit_code=1
  elif $passed; then
    echo "ok $exercise ($language)"
  elif expected_failure "$exercise/$language"; then
    echo "expected failure $exercise ($language)"
  else
    echo "FAIL $exercise ($language)"
    cat "$details"
    grep -q "expected" "$details" || tail -n 20 "$out"
    exit_code=1
  fi
done < "$tmp/list"

exit $exit_code
