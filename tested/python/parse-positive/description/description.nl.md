Schrijf een functie `parse_positive` die een string als argument aanvaardt.
Als de string een geheel getal groter dan nul voorstelt, moet de functie dat getal teruggeven als integer.
In alle andere gevallen moet de functie een `ValueError` opwerpen met de boodschap `not a positive number`.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> parse_positive("42")
42
>>> parse_positive("-3")
Traceback (most recent call last):
  ...
ValueError: not a positive number
```
