In deze oefening vat je een jaar aan neerslagmetingen samen met
[pandas](https://pandas.pydata.org/) en teken je het resultaat als een
staafdiagram met [matplotlib](https://matplotlib.org/).

Elke meting is een paar `[maand, neerslag]`, waarbij `maand` een geheel getal is
van `1` (januari) tot `12` (december) en `neerslag` een hoeveelheid in
millimeter. Er kunnen meerdere metingen per maand zijn, in willekeurige
volgorde.

### Opdracht

Schrijf een functie `rainfall_chart(records)` die:

1. de **totale** neerslag per maand berekent en teruggeeft als een lijst van
   twaalf gehele getallen, geordend van januari tot december. Maanden zonder
   meting krijgen totaal `0`.
2. een **staafdiagram** van die maandtotalen tekent (de maand op de horizontale
   as, de totale neerslag op de verticale as) en het toont met `plt.show()`.

### Voorbeeld

```python
>>> rainfall_chart([[1, 12], [1, 8], [2, 5], [2, 5], [3, 20]])
[20, 10, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

(en er wordt een staafdiagram getekend)

> Wanneer je indient, vangt de judge de grafiek op die je code tekent en toont
> ze opnieuw in de feedback onder de testresultaten, zodat je precies ziet wat
> je code heeft gemaakt.
