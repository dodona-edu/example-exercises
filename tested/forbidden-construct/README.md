# Sum to n (forbidding a construct)

Demonstrates how to reject a submission because of **how it is written**, not
because of what it returns. The student writes `sum_to(n)`, and the exercise
insists the sum is built with a `for` loop: a `while` loop, a call to the
built-in `sum`, and a closed-form formula are all refused, even though each of
them returns exactly the right number.

This is the usual answer to "my students must use a loop here, not `sum`" or
"this one has to be recursive". TESTed grades behaviour, so behaviour tests
alone cannot tell these solutions apart.

## How it works

A `custom_check` oracle normally only sees the expected and actual value. But
when the oracle declares which languages it supports, TESTed also hands it the
path of the submitted file:

```python
# tested/oracles/programmed.py
submission_path=(config.bundle.config.source if channel.oracle.languages else None)
```

So the `languages` key in `evaluation/suite.yaml` is what makes this work, and
dropping it silently turns the check off (`submission_path` becomes `None`):

```yaml
- tab: "Source check"
  testcases:
    - description: "builds the sum with a for loop, without a while loop or sum"
      expression:
        python: "True"
      return: !oracle
        value: true
        oracle: "custom_check"
        file: "source_check.py"
        name: "check_source"
        languages: ["python"]     # <- without this, there is no source to read
```

The testcase itself is a throwaway: it evaluates `True` and compares it to
`true`, purely so that an oracle runs. `evaluation/source_check.py` ignores
both values, opens `context.submission_path`, parses it with `ast` and walks
the tree.

The source check lives in **its own tab**, next to the ordinary behaviour tests
in the "Sum" tab. It is an extra requirement, not a replacement: a solution
that loops correctly but computes the wrong sum still fails on behaviour, and a
solution that computes the right sum the forbidden way fails only the "Source
check" tab.

## Adapting it

Everything that encodes the rule sits in three constants at the top of
`evaluation/source_check.py`. The walking code below them is generic, so
forbidding something else is a one-line edit:

```python
FORBIDDEN_NODES = {ast.While: "a while loop"}          # syntax that is refused
FORBIDDEN_CALLS = {"sum": "the built-in function sum"} # calls that are refused
REQUIRED_NODES  = {ast.For: "a for loop"}              # syntax that must appear
```

To forbid recursion helpers instead, put their names in `FORBIDDEN_CALLS`; to
forbid imports, add `ast.Import` to `FORBIDDEN_NODES`; to demand a `try` block,
add `ast.Try` to `REQUIRED_NODES`. Update `RULE` and `EXPECTED` in the same
block so the feedback keeps matching the rule, and state the rule in the
description too.

## Limits

Worth knowing before reusing this:

- **It is Python-specific.** The oracle parses Python with `ast`, and
  `languages: ["python"]` says so. Unlike most exercises in `tested/`, this one
  does not port to another language by flipping `programming_language`: you
  would have to parse that language instead.
- **It checks syntax, not semantics.** The tree is all it sees. A `for` loop
  that never runs still counts as a `for` loop.
- **An unparseable submission never reaches the check.** TESTed compiles the
  submission first and escalates a compilation error before any oracle runs, so
  a syntax error already fails the submission on its own. The oracle still
  handles `SyntaxError`, and accepts when `submission_path` is missing or
  unreadable rather than punishing a student for a judge limitation, but those
  branches are safety nets rather than the normal path.
- **A determined student can evade it.** Building the forbidden code as a
  string and running it through `exec`, `eval` or `compile` leaves no `While`
  node behind. You can forbid those names too, but there is no version of this
  that a motivated student cannot work around. It is a guardrail that keeps
  honest students on the intended path, not a sandbox.
- **`REQUIRED_NODES` rejects legitimate answers on purpose.** Requiring a `for`
  loop is what closes the "just return the constant" hole, but it also refuses
  `n * (n + 1) // 2`, which is a perfectly good solution to the stated problem,
  and it refuses comprehensions, because `ast.For` matches a `for` statement
  and not an `ast.comprehension`. That is a deliberate trade-off for an
  exercise whose point is practising the loop. Say so in the description, as
  this one does, rather than letting a student discover it from a failing test.
  If you only want to forbid things, set `REQUIRED_NODES = {}`.

## Why not a linter?

Dodona runs pylint on Python submissions, so it is a fair question. It cannot
do this job, for two separate reasons:

1. Pylint has no general way to forbid a construct. It can blacklist a few
   named builtins through the `bad-builtin` extension, but there is no
   "disallow `while`" message to switch on.
2. More fundamentally, the judge only turns linter output into feedback:
   `run_linter` in `tested/judge/linter.py` adds `AppendMessage` and
   `AnnotateCode` to the output collector, and never a status. A linter finding
   shows up as an annotation in the margin and leaves the verdict untouched, so
   it can never make a submission wrong.

An oracle, by contrast, returns a real verdict.
