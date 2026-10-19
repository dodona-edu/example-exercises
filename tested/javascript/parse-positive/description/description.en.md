Write a function `parsePositive` that receives a string as argument.
If the string represents a whole number greater than zero, the function should return that number.
Otherwise, the function should throw an `Error` with the message `not a positive number`.

### Example

```console?lang=javascript&prompt=>
> parsePositive("42")
42
> parsePositive("-3")
Uncaught Error: not a positive number
```
