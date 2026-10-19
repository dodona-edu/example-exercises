Schrijf een klasse `Stack` die getallen bijhoudt: het laatste getal dat je toevoegt, is het eerste dat je terugkrijgt.

De klasse moet de volgende methoden ondersteunen:

- Een methode `push(value)` die een getal bovenaan de stapel plaatst.
- Een methode `pop()` die het getal bovenaan de stapel verwijdert en teruggeeft.
- Een methode `peek()` die het getal bovenaan de stapel teruggeeft zonder het te verwijderen.
- Een methode `size()` die teruggeeft hoeveel getallen er op de stapel liggen.

Gebruik geen `export`: de oplossing wordt samen met de tests gecompileerd.

### Voorbeeld

```console?lang=typescript&prompt=>
> const stack = new Stack();
> stack.push(1);
> stack.push(2);
> stack.peek()
2
> stack.size()
2
> stack.pop()
2
> stack.size()
1
```
