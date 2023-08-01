Write a program `sum`, which prints the sum of some numbers to `stdout`.
These numbers will be given as program arguments to the program.

If one of the numbers is not an integer, the error message `invalid arguments` should be written to `stderr`.
In this case, the exit code of the program should be `1`.

### Example

```console
$ ./sum -1 -23 72 84 -38 -61 49 45
127
$ ./sum
0
$ ./sum spam eggs beacon
invalid arguments
```
