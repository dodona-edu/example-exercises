Write a function `sum_to` that receives an integer `n` as argument.
The function should return the sum of all integers from 1 up to and including `n`.
If `n` is smaller than 1, the function should return 0.

Build the sum step by step with a `for` loop.
Solutions that use a `while` loop, that call the built-in function `sum`, or that compute the answer with a formula are not accepted.

### Example

```console?lang=python&prompt=>>>
>>> sum_to(5)
15
>>> sum_to(1)
1
>>> sum_to(0)
0
```
