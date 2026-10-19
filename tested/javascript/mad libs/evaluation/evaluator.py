import re

# noinspection PyUnresolvedReferences
from evaluation_utils import EvaluationResult


def suggest(category, categories):
    candidates = categories[category.lower()]
    if re.fullmatch(r"[A-Z]+", category):
        return [word.upper() for word in candidates]
    if re.fullmatch(r"[A-Z][a-z]*", category):
        return [word[:1].upper() + word[1:] for word in candidates]
    return candidates


def fillings(madlib, categories):
    fragments = madlib.split("_")
    madlibs = [""]
    for i in range(len(fragments) // 2):
        candidates = suggest(fragments[2 * i + 1], categories)
        madlibs = [m + fragments[2 * i] + c for m in madlibs for c in candidates]
    return [m + fragments[-1] for m in madlibs]


def check_mad_libs(context, madlib, categories):
    correct = context.actual in fillings(madlib, categories)
    return EvaluationResult(
        result=correct,
        dsl_expected=repr(context.actual) if correct else None,
    )
