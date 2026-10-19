import ast

# noinspection PyUnresolvedReferences
from evaluation_utils import EvaluationResult, Message

# ---------------------------------------------------------------------------
# The rule.
#
# This block is the only thing you have to edit to forbid something else. Each
# entry maps a check to the words used in the feedback, so the message stays
# readable whatever you put here. The code below is generic: it walks the
# syntax tree and applies whatever these four constants contain.
# ---------------------------------------------------------------------------

# Syntax the submission may not contain. Keys are ast node classes.
# Examples: ast.While (while loop), ast.ListComp (list comprehension),
# ast.Lambda, ast.Global, ast.Try. Imports take two node classes: ast.Import
# matches "import x", ast.ImportFrom matches "from x import y", so forbidding
# imports means adding both.
FORBIDDEN_NODES = {
    ast.While: "a while loop",
}

# Functions the submission may not call, by the name at the call site.
# Both sum(...) and builtins.sum(...) match the key "sum".
FORBIDDEN_CALLS = {
    "sum": "the built-in function sum",
}

# Syntax the submission must contain at least once. Leave this empty ({}) if
# you only want to forbid things. Note that ast.For matches a for statement,
# not a comprehension: add ast.comprehension if those should count too.
REQUIRED_NODES = {
    ast.For: "a for loop",
}

# The function REQUIRED_NODES has to appear in, or None to search the whole
# file. The two kinds of check are scoped differently on purpose: the forbidden
# checks always look at the whole file, so a forbidden construct cannot be
# hidden in a helper, while the required checks look inside this one function,
# so a for loop in an unrelated helper does not satisfy a rule about the
# function being graded. A submission that does not define the function at all
# falls back to the whole file; the behaviour tests already fail it.
REQUIRED_IN_FUNCTION = "sum_to"

# One sentence stating the rule, shown to the student when the check fails.
RULE = (
    "Build the sum with a for loop. A while loop, the built-in function sum, "
    "and a closed-form formula are not accepted for this exercise."
)

# How the accepted shape is described in the feedback table.
EXPECTED = "a solution that builds the sum with a for loop"


def _rejected(actual):
    return EvaluationResult(
        result=False,
        readable_expected=EXPECTED,
        readable_actual=actual,
        messages=[Message(description=RULE, format="text")],
    )


def _accepted():
    return EvaluationResult(
        result=True,
        readable_expected=EXPECTED,
        readable_actual=EXPECTED,
    )


def _called_name(func):
    """The name a call refers to, or None if it cannot be determined statically.

    ``sum(...)`` is an ast.Name, ``builtins.sum(...)`` an ast.Attribute. Both
    yield "sum", so qualifying a call does not sneak it past the check.
    """
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def _graded_function(tree):
    """The definition of REQUIRED_IN_FUNCTION, or None if the file lacks it."""
    if not REQUIRED_IN_FUNCTION:
        return None
    for node in ast.walk(tree):
        is_function = isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        if is_function and node.name == REQUIRED_IN_FUNCTION:
            return node
    return None


def check_source(context):
    """Check how the submission is written, not what it returns.

    The behaviour tests cannot tell an accepted solution from a forbidden one:
    a while loop sums just as correctly as a for loop. TESTed hands a custom
    check the path of the submitted file in ``context.submission_path``, but
    only when the oracle declares which languages it supports, so the test
    suite sets ``languages: ["python"]`` on this oracle. See
    ``tested/oracles/programmed.py`` in the judge.
    """
    path = getattr(context, "submission_path", None)
    if not path:
        # No source to inspect. Never fail a student over a judge limitation.
        return _accepted()

    try:
        with open(path, "r", encoding="utf-8") as handle:
            source = handle.read()
    except (OSError, UnicodeDecodeError):
        # Same reasoning: the source should be there and should be UTF-8, but
        # if it cannot be read or decoded, the student is not the one to blame.
        return _accepted()

    try:
        tree = ast.parse(source)
    except SyntaxError as error:
        return _rejected(
            f"a solution Python could not parse ({error.msg}, line {error.lineno})"
        )

    nodes = list(ast.walk(tree))

    # The forbidden checks look at the whole file (see REQUIRED_IN_FUNCTION).
    for node_type, description in FORBIDDEN_NODES.items():
        if any(isinstance(node, node_type) for node in nodes):
            return _rejected(f"a solution that uses {description}")

    for node in nodes:
        if isinstance(node, ast.Call):
            name = _called_name(node.func)
            if name in FORBIDDEN_CALLS:
                return _rejected(f"a solution that calls {FORBIDDEN_CALLS[name]}")

    # The required checks look inside the graded function only, falling back to
    # the whole file when the submission does not define it.
    graded = _graded_function(tree)
    required_nodes = list(ast.walk(graded)) if graded else nodes

    for node_type, description in REQUIRED_NODES.items():
        if not any(isinstance(node, node_type) for node in required_nodes):
            if graded:
                return _rejected(
                    f"a solution whose {graded.name} does not use {description}"
                )
            return _rejected(f"a solution without {description}")

    return _accepted()
