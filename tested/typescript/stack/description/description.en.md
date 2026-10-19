Write a class `Stack` that stores numbers: the last number you add is the first one you get back.

The class should support the following methods:

- A method `push(value)` which adds a number to the top of the stack.
- A method `pop()` which removes the number on top of the stack and returns it.
- A method `peek()` which returns the number on top of the stack without removing it.
- A method `size()` which returns how many numbers are on the stack.

Submissions are compiled together with the tests, so don't use `export`.

### Example

```console?lang=typescript&prompt=>
> const stack = new Stack();
> stack.push(1);
> stack.push(2);
> stack.peek()
2
> stack.size()
2
> stack.pop()
2
> stack.size()
1
```
