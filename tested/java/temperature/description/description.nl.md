Schrijf een klasse `Temperature` die een temperatuur in graden Celsius bijhoudt.

De constructor krijgt de temperatuur mee als `double`.
Als de temperatuur lager is dan het absolute nulpunt (-273,15 graden Celsius),
moet de constructor een `IllegalArgumentException` gooien met als boodschap `below absolute zero`.

Daarnaast moet de klasse de volgende methode ondersteunen:

- Een methode `toFahrenheit()` die de temperatuur in graden Fahrenheit teruggeeft als `double`.

Declareer de klasse zonder `public`: TESTed bewaart je code als `Submission.java`, en Java staat enkel een publieke klasse toe in een bestand met dezelfde naam.

### Voorbeeld

```java
Temperature water = new Temperature(100.0);
System.out.println(water.toFahrenheit());  // 212.0
Temperature impossible = new Temperature(-300.0);  // gooit IllegalArgumentException
```
