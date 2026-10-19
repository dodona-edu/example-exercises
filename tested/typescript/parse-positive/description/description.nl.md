Schrijf een functie `parsePositive` die een string als argument aanvaardt.
Als de string een geheel getal groter dan nul voorstelt, moet de functie dat getal teruggeven.
Anders moet de functie een `Error` gooien met de boodschap `not a positive number`.

Gebruik geen `export`: de oplossing wordt samen met de tests gecompileerd.

### Voorbeeld

```console?lang=typescript&prompt=>
> parsePositive("42")
42
> parsePositive("-3")
Error: not a positive number
```
