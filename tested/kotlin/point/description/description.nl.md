Schrijf een data class `Point` die een punt in het vlak voorstelt.
Een punt heeft twee eigenschappen `x` en `y` van het type `Double`, die meegegeven worden aan de constructor.

Daarnaast moet de klasse de volgende methode ondersteunen:

- Een methode `distanceTo(other)` die de afstand tussen dit punt en het punt `other` teruggeeft, als een `Double`.

### Voorbeeld

```console?lang=kotlin&prompt=>>>
>>> val a = Point(0.0, 0.0)
>>> a.distanceTo(Point(3.0, 4.0))
5.0
```
