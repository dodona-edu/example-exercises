Schrijf een functie `smallest` die twee gehele getallen als argumenten aanvaardt.
Deze functie moet het kleinste van die twee teruggeven.

### Voorbeeld

```console?lang=python&prompt=>>>
>>> smallest(5, 6)
5
```

### Eender welke programmeertaal

Dezelfde testen werken in elke programmeertaal die TESTed ondersteunt, behalve Bash.
Deze repository bevat een oplossing in al die talen in de map `solution/`.

Dodona laat per oefening één programmeertaal toe, dus studenten kunnen niet per indiening een taal kiezen.
Een lesgever kiest de taal door `programming_language` in te stellen in `config.json`.
Zolang dat niet gebeurt, staat deze oefening in Python.

Wat TESTed verwacht per taal:

| Taal | Vereisten |
| --- | --- |
| Python, JavaScript, TypeScript, Kotlin, Haskell | Een functie met de naam `smallest`. |
| C, C++ | Een functie met de naam `smallest`. Een `main` is niet nodig. |
| Java | Een `public static` methode `smallest` in een klasse met de naam `Submission`. |
| C# | Een `public static` methode `Smallest` (met hoofdletter S) in een klasse met de naam `Submission`. |

Sommige talen hebben extra vereisten:

- Haskell: geen `module`-regel. Zolang [universal-judge#568](https://github.com/dodona-edu/universal-judge/issues/568) niet opgelost is, genereert TESTed ongeldige Haskell voor deze testen (`smallest 5 :: Int 6 :: Int`), dus deze oefening compileert in Haskell nog niet.
- TypeScript: geen `export`.
- Bash wordt niet ondersteund voor deze oefening, omdat TESTed in Bash enkel tekstargumenten aan een functie kan doorgeven.
