Write a data class `Point` that represents a point in the plane.
A point has two properties `x` and `y` of type `Double`, which are passed to the constructor.

The class should also support the following method:

- A method `distanceTo(other)` which returns the distance between this point and the point `other`, as a `Double`.

### Example

```console?lang=kotlin&prompt=>>>
>>> val a = Point(0.0, 0.0)
>>> a.distanceTo(Point(3.0, 4.0))
5.0
```
