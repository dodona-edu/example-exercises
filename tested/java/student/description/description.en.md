Write a class `Student` that keeps track of the grades of a student.

The constructor receives the name of the student as a `String`.
The class should also support the following methods:

- A method `getName()` which returns the name of the student.
- A method `addGrade(int grade)` which adds a grade for the student.
- A method `average()` which returns the average of all grades added so far as a `double`.

Declare the class without `public`: TESTed saves your code as `Submission.java`, and Java only allows a public class in a file with the same name.

### Example

```java
Student student = new Student("Alice");
student.addGrade(12);
student.addGrade(15);
System.out.println(student.getName());  // Alice
System.out.println(student.average());  // 13.5
```
