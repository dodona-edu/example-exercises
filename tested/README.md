# Example exercises for TESTed

(Some of) these exercises are explained in detail in our documentation:

- http://docs.dodona.be/guides/exercises/examples/input-output
- http://docs.dodona.be/guides/exercises/examples/function
- http://docs.dodona.be/guides/exercises/examples/class
- http://docs.dodona.be/guides/exercises/examples/command-line

## One suite, every language

In [`echo-name/`](echo-name/) and [`smallest/`](smallest/), one test suite judges every programming language TESTed supports (`smallest`: all but Bash).
Their `solution/` directory has a solution in each of those languages.
Dodona allows one programming language per exercise: set `programming_language` in `config.json` to pick one (Python by default, from `dirconfig.json`).
`.github/workflows/examples.yml` runs every solution against its suite, here and in the language directories.

## A directory per language

These directories hold exercises typical for one language, each showing one TESTed feature (return values, objects, expected exceptions, program arguments and exit codes, files, stdin).
Their `dirconfig.json` sets the programming language.

- [`bash/`](bash/)
- [`c/`](c/)
- [`cpp/`](cpp/)
- [`csharp/`](csharp/)
- [`haskell/`](haskell/)
- [`java/`](java/)
- [`javascript/`](javascript/)
- [`kotlin/`](kotlin/)
- [`python/`](python/)
- [`typescript/`](typescript/)

`python/forbidden-construct` checks how a submission is written by parsing it with Python's `ast` module, so its oracle only works for Python.
