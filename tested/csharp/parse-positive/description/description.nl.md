Schrijf een functie `ParsePositive` die een string als argument aanvaardt.
Als de string een geheel getal groter dan nul voorstelt, moet de functie dat getal als integer teruggeven.
In alle andere gevallen moet de functie een `ArgumentException` gooien met de boodschap `not a positive number`.

De functie moet een `public static` methode zijn van een klasse met de naam `Submission`.

### Voorbeeld

```console?lang=csharp&prompt=>
> Submission.ParsePositive("42")
42
> Submission.ParsePositive("-3")
System.ArgumentException: not a positive number
```
