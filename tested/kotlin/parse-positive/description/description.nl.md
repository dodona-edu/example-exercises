Schrijf een functie `parsePositive` die een string als argument aanvaardt.
Als de string een geheel getal groter dan nul voorstelt, moet de functie dat getal teruggeven als een `Int`.
In alle andere gevallen moet de functie een `IllegalArgumentException` werpen met als boodschap `not a positive number`.

### Voorbeeld

```console?lang=kotlin&prompt=>>>
>>> parsePositive("42")
42
>>> parsePositive("-3")
java.lang.IllegalArgumentException: not a positive number
```
