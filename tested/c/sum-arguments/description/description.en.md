Write a C program that prints the sum of its command-line arguments to `stdout`.
The arguments are integers.

If one of the arguments is not an integer, the program should write the error message `invalid arguments` to `stderr` and exit with exit code `1`.

### Example

```console
$ ./program -1 -23 72 84 -38 -61 49 45
127
$ ./program
0
$ ./program spam eggs bacon
invalid arguments
```
