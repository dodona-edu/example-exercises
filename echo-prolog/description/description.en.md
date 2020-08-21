Write a predicate `echo` that is true when the second argument unifies with the first argument.

### voorbeeld

```prolog
>> echo(5, 5).
true
>> echo("ok", "not ok").
false
>> echo(panda, X).
X = panda.
```
