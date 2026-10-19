Write a function `parse_positive` that receives a text as argument.
If the text is a whole number greater than zero, the function should return that number as an `int`.
Otherwise it should throw a `std::invalid_argument` with the message `not a positive number`.

Do not write a `main` function: TESTed calls your function itself.

### Example

```cpp
parse_positive("42"); // returns 42
parse_positive("-3"); // throws std::invalid_argument("not a positive number")
```
