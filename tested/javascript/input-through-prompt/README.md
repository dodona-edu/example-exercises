# Input through prompt

This exercise demonstrates how to use `prompt()` in a JavaScript exercise judged by TESTed.

## The problem

TESTed runs JavaScript in Node.js, where `prompt()` does not exist. However, many beginner JavaScript tutorials and browser-based environments use `prompt()` to read user input. To support exercises written in this style, a shim is needed.

## The shim

Each test context in `evaluation/suite.json` contains a `before.javascript.data` block with the following code:

```javascript
const _fs = require('fs');
const _lines = _fs.readFileSync(0, 'utf8').trim().split('\n');
let _i = 0;
globalThis.prompt = function(msg) { return _lines[_i++]; };
```

**How it works:**

1. `_fs.readFileSync(0, 'utf8')` reads all of stdin (file descriptor `0`) synchronously.
2. The result is split into individual lines.
3. `globalThis.prompt` is defined as a function that returns the next line each time it is called, simulating the browser `prompt()` behaviour.

## Why each test case needs its own context

Each context in TESTed is a fresh execution of the student's program. Because this exercise tests different inputs to the same program, each test case represents a separate run — and TESTed only allows one `main_call: true` per context. That constraint is why each test case lives in its own context.

## Suite structure

```
before.javascript.data  ← installs the prompt() shim
testcases[0]
  input.main_call       ← runs the student's script as a program
  input.stdin           ← the value that prompt() will return
  output.stdout         ← expected console.log() output
```
