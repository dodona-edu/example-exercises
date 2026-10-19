Write a function `parsePositive` that receives a string as its argument.
If the string is a whole number greater than zero, the function should return that number.
Otherwise, the function should throw an `Error` with the message `not a positive number`.

Submissions are compiled together with the tests, so don't use `export`.

### Example

```console?lang=typescript&prompt=>
> parsePositive("42")
42
> parsePositive("-3")
Error: not a positive number
```
