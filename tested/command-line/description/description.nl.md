Schrijf een programma `sum` dat de som van een reeks getallen uitschrijft op `stdout`.
Deze getallen worden als argumenten aan het programma meegegeven.

Als een van de argumenten geen geheel getal is, moet een foutboodschap uitgeschreven worden op `stderr`: `invalid arguments`.
In dat geval moet de exitcode van het programma ook `1` zijn.

### Voorbeeld

```console
$ ./sum -1 -23 72 84 -38 -61 49 45
127
$ ./sum
0
$ ./sum spam eggs beacon
invalid arguments
```
