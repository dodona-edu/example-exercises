Write a Bash script that receives one argument: an age.

If the argument is a non-negative integer, the script prints `Age: [AGE]` to `stdout`,
where `[AGE]` is the given age.

Otherwise, the script writes the error message `invalid age` to `stderr`.
In this case, the exit code of the script must also be `1`.

### Example

```console
$ bash check-age.sh 25
Age: 25
$ bash check-age.sh abc
invalid age
```
