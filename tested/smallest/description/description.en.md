Write a function `smallest` that accepts two integers as arguments.
The function must return the smaller of the two.

### Example

```console?lang=python&prompt=>>>
>>> smallest(5, 6)
5
```

### Any programming language

The same tests work in every programming language that TESTed supports, except Bash.
This repository has a solution in each of those languages in the `solution/` directory.

Dodona allows one programming language per exercise, so students can't choose a language for each submission.
A teacher picks the language by setting `programming_language` in `config.json`.
Until then, this exercise is in Python.

What TESTed expects per language:

| Language | Requirements |
| --- | --- |
| Python, JavaScript, TypeScript, Kotlin, Haskell | A function named `smallest`. |
| C, C++ | A function named `smallest`. No `main` is needed. |
| Java | A `public static` method `smallest` in a class named `Submission`. |
| C# | A `public static` method `Smallest` (capital S) in a class named `Submission`. |

Some languages have extra requirements:

- Haskell: no `module` line. Until [universal-judge#568](https://github.com/dodona-edu/universal-judge/issues/568) is fixed, TESTed generates invalid Haskell for these tests (`smallest 5 :: Int 6 :: Int`), so this exercise doesn't compile in Haskell yet.
- TypeScript: no `export`.
- Bash is not supported for this exercise, because TESTed's Bash can only pass text arguments to a function.
