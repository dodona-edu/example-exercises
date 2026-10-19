Schrijf een functie `parse_positive` die een tekst als argument aanvaardt.
Als de tekst een geheel getal groter dan nul voorstelt, moet de functie dat getal teruggeven als `int`.
Anders moet de functie een `std::invalid_argument` gooien met de boodschap `not a positive number`.

Schrijf geen `main`-functie: TESTed roept je functie zelf aan.

### Voorbeeld

```cpp
parse_positive("42"); // geeft 42 terug
parse_positive("-3"); // gooit std::invalid_argument("not a positive number")
```
