Schrijf een C-programma dat de som van zijn opdrachtlijnargumenten uitschrijft naar `stdout`.
De argumenten zijn gehele getallen.

Als een van de argumenten geen geheel getal is, moet het programma de foutboodschap `invalid arguments` uitschrijven naar `stderr` en eindigen met exitcode `1`.

### Voorbeeld

```console
$ ./programma -1 -23 72 84 -38 -61 49 45
127
$ ./programma
0
$ ./programma spam eggs bacon
invalid arguments
```
