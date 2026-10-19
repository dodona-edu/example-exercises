Write a function `ParsePositive` that receives a string as argument.
If the string represents a whole number greater than zero, the function should return that number as an integer.
Otherwise, the function must throw an `ArgumentException` with the message `not a positive number`.

The function must be a `public static` method of a class named `Submission`.

### Example

```console?lang=csharp&prompt=>
> Submission.ParsePositive("42")
42
> Submission.ParsePositive("-3")
System.ArgumentException: not a positive number
```
