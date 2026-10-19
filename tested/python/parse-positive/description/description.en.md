Write a function `parse_positive` that receives a string as argument.
If the string represents a whole number greater than zero, the function should return that number as an integer.
Otherwise, the function should raise a `ValueError` with the message `not a positive number`.

### Example

```console?lang=python&prompt=>>>
>>> parse_positive("42")
42
>>> parse_positive("-3")
Traceback (most recent call last):
  ...
ValueError: not a positive number
```
