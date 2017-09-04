Binnen het ISBN-10 (*International Standard Book Numbering*) systeem dat
tot eind 2006 gebruikt werd, kreeg elk boek een unieke code toegewezen
die bestaat uit 10 cijfers. De eerste 9 daarvan geven informatie over
het boek zelf, terwijl het laatste louter een controlecijfer is dat
dient om foutieve ISBN-10 codes te detecteren.

![ISBN](media/ISBN.gif "ISBN"){:height="140"}


Indien \$\$x\_1, \\ldots, x\_9\$\$ de eerste 9 cijfers van een ISBN-10
code voorstellen, dan wordt het controlecijfer \$\$x\_{10}\$\$ als volgt
berekend: \\\[x\_{10} = (x\_1+ 2x\_2+ 3x\_3+ 4x\_4+ 5x\_5+ 6x\_6+ 7x\_7+
8x\_8+ 9x\_9)\\!\\!\\!\\!\\mod{11}\\\] Het controlecijfer
\$\$x\_{10}\$\$ kan m.a.w. de waarden 0 tot en met 10 aannemen. Gevraagd
wordt om een programma te schrijven dat het controlecijfer berekent op
basis van de eerste negen cijfers van een ISBN-10 code.

### Invoer

Negen natuurlijke getallen \$\$x\_1, \\ldots, x\_9\$\$ (\$\$0 \\leq
x\_1, \\ldots, x\_9 \\leq 9\$\$), elk op een afzonderlijke regel. Deze
stellen de eerste negen cijfers van een gegeven ISBN-10 code voor.

### Uitvoer

Eén regel die een natuurlijk getal bevat: het controlecijfer dat
correspondeert met de gegeven cijfers van een ISBN-10 code. Zorg ervoor
dat dit natuurlijk getal geen voorloopnullen heeft.

### Voorbeeld

**Invoer:**

    9
    9
    7
    1
    5
    0
    2
    1
    0

**Uitvoer:**

    0

### Pythia spreekt …

In onderstaande video legt Pythia uit hoe je deze opgave kunt aanpakken.
Bekijk de video als opstapje naar het oplossen van de oefeningen over
[variabelen, expressies en
statements](https://dodona.ugent.be/nl/exercises/?filter=opgaven/reeks01).

<iframe src="https://www.youtube.com/embed/Ne35kBQNLXg" allowfullscreen="" frameborder="0" height="315" width="560"></iframe>

### Epiloog

![evolution into
barcode](media/evaluation_barcode.jpg "evolution into barcode"){:height="320px"}
