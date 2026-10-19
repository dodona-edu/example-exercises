Write a function `parsePositive` that receives a string as argument.
If the string represents a whole number greater than zero, the function should return that number as an `Int`.
Otherwise, the function should throw an `IllegalArgumentException` with the message `not a positive number`.

### Example

```console?lang=kotlin&prompt=>>>
>>> parsePositive("42")
42
>>> parsePositive("-3")
java.lang.IllegalArgumentException: not a positive number
```
