Write a class `Counter`, which can be used to count.

When an instance of the class is created, the start value of the counter is passed to the constructor.
The default start value is 0.

The class should also support the following methods:

- A method `count()` which increases the count by one.
  The method must return its own instance.
- A method `report()` which writes the current count to `stdout`.
- 
### Example

```console?lang=python&prompt=>>>
>>> counter = Counter(5)
>>> counter.report()
5
>>> counter.count()
>>> counter.report()
6
>>> counter.count().count().count().count().report()
10
```
```
