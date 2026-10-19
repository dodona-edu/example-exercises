Schrijf een Bash-script dat één argument krijgt: een leeftijd.

Als het argument een niet-negatief geheel getal is, schrijft het script `Age: [LEEFTIJD]` uit naar `stdout`,
waarbij `[LEEFTIJD]` de opgegeven leeftijd is.

Anders schrijft het script de foutboodschap `invalid age` uit naar `stderr`.
In dat geval moet de exitcode van het script ook `1` zijn.

### Voorbeeld

```console
$ bash check-age.sh 25
Age: 25
$ bash check-age.sh abc
invalid age
```
