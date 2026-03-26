In deze oefening gebruik je de `turtle`-module om een **rups** te tekenen.

Je programma moet:

1. Een **geheel getal** inlezen: het aantal lichaamssegmenten.
2. Een rups tekenen met precies dat aantal segmenten.

Je rups moet minstens het volgende bevatten:
- Het juiste aantal **lichaamssegmenten** (cirkels werken prima!)
- Een **gezichtje** op het hoofdsegment (ogen en een mond)
- Twee **voelsprieten**

Wees gerust creatief! Je kan bijvoorbeeld toevoegen:
- Kleurrijke segmenten — wissel kleuren af of gebruik een kleurverloop
- Kleine pootjes onder elk segment
- Een leuke achtergrond met gras of bloemen
- Vlekken of patronen op het lichaam

Hier is een mogelijk resultaat met 6 segmenten ter inspiratie — jouw rups mag er helemaal anders uitzien!

![Voorbeeld rups](media/caterpillar.svg){:height="50%" width="50%"}{: style="border-style: inset"}

## Tips

Enkele nuttige `turtle`-functies:

- `turtle.circle(straal)` — tekent een volledige cirkel tegen de klok in
- `turtle.begin_fill()` / `turtle.end_fill()` — vul een vorm in met `turtle.fillcolor("kleur")`
- `turtle.penup()` / `turtle.pendown()` / `turtle.goto(x, y)` — verplaatsen zonder te tekenen
- `turtle.setheading(hoek)` — wijs de turtle in een bepaalde richting (0 = rechts, 90 = omhoog)
- `turtle.forward(afstand)` — beweeg de turtle vooruit (handig voor voelsprieten!)

{: .callout.callout-info}
> #### Automated feedback
>
> Your code will be checked for errors and common code issues, but the correctness of your drawing is not verified automatically. Make sure to look at your own output and verify that it matches what the assignment asks for.
