Schrijf een klasse `Counter`, waarmee we een telling kunnen doen.

Als een instantie van de klasse aangemaakt wordt,
kan de beginwaarde meegegeven worden aan de constructor.
De standaardwaarde is 0.

Daarnaast moet de klasse de volgende methoden ondersteunen:

- Een methode `count()` die de telling met één verhoogt.
  De methode moet de eigen instantie teruggeven.
- Een methode `report()` die de huidige telling schrijft naar `stdout`.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> counter = Counter(5)
>>> counter.report()
5
>>> counter.count()
>>> counter.report()
6
>>> counter.count().count().count().count().report()
10
```
