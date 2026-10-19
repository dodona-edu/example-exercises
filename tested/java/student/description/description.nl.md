Schrijf een klasse `Student` die de punten van een student bijhoudt.

De constructor krijgt de naam van de student mee als `String`.
Daarnaast moet de klasse de volgende methoden ondersteunen:

- Een methode `getName()` die de naam van de student teruggeeft.
- Een methode `addGrade(int grade)` die een punt voor de student toevoegt.
- Een methode `average()` die het gemiddelde van alle tot nu toe toegevoegde punten teruggeeft als `double`.

Declareer de klasse zonder `public`: TESTed bewaart je code als `Submission.java`, en Java staat enkel een publieke klasse toe in een bestand met dezelfde naam.

### Voorbeeld

```java
Student student = new Student("Alice");
student.addGrade(12);
student.addGrade(15);
System.out.println(student.getName());  // Alice
System.out.println(student.average());  // 13.5
```
