Schrijf een functie `parsePositive` die een string als argument aanvaardt.
Als de string een geheel getal groter dan nul voorstelt, moet de functie dat getal teruggeven.
Anders moet de functie een `Error` opgooien met de boodschap `not a positive number`.

### Voorbeeld

```console?lang=javascript&prompt=>
> parsePositive("42")
42
> parsePositive("-3")
Uncaught Error: not a positive number
```
