Write a class `Temperature` that stores a temperature in degrees Celsius.

The constructor receives the temperature as a `double`.
If the temperature is below absolute zero (-273.15 degrees Celsius),
the constructor should throw an `IllegalArgumentException` with the message `below absolute zero`.

The class should also support the following method:

- A method `toFahrenheit()` which returns the temperature in degrees Fahrenheit as a `double`.

Declare the class without `public`: TESTed saves your code as `Submission.java`, and Java only allows a public class in a file with the same name.

### Example

```java
Temperature water = new Temperature(100.0);
System.out.println(water.toFahrenheit());  // 212.0
Temperature impossible = new Temperature(-300.0);  // throws IllegalArgumentException
```
