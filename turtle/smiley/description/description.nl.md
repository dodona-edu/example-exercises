Laat je creativiteit de vrije loop! In deze oefening gebruik je de `turtle`-module om een **smiley** te tekenen. Maak er iets unieks van — er is geen enkel juist antwoord.

Je smiley moet minstens bevatten:
- Een **gezicht** (een cirkel is een goed begin!)
- Twee **ogen**
- Een **glimlach**

Maar daar hoef je niet bij te stoppen! Je kunt ook toevoegen:
- Kleuren — geef je smiley een eigen look
- Wenkbrauwen — verrast, blij of boos?
- Een neus
- Blosjes op de wangen
- Een hoed, haar of andere accessoires
- Een leuke achtergrond

Experimenteer, speel en geniet ervan. Hier is één mogelijk resultaat ter inspiratie — het jouwe mag er helemaal anders uitzien!

![Voorbeeld van een smiley](media/smiley.svg){:height="50%" width="50%"}{: style="border-style: inset"}

## Tips

Enkele nuttige `turtle`-functies voor het tekenen van cirkels en bogen:

- `turtle.circle(straal)` — tekent een volledige cirkel tegen de klok in
- `turtle.circle(straal, hoek)` — tekent een boog van `hoek` graden
- `turtle.begin_fill()` / `turtle.end_fill()` — vult een vorm in met de huidige kleur
- `turtle.fillcolor("yellow")` — stel de vulkleur in
- `turtle.penup()` / `turtle.pendown()` / `turtle.goto(x, y)` — beweeg zonder te tekenen
- `turtle.setheading(hoek)` — wijs de turtle in een bepaalde richting (0 = rechts, 90 = omhoog)

{: .callout.callout-info}
> #### Automatische feedback
>
> Je code wordt gecontroleerd op syntaxfouten en veelvoorkomende codeproblemen, maar de correctheid van je tekening wordt niet automatisch geverifieerd — dit is slechts een indicatie of je code syntactisch correct is. Zorg er zelf voor dat je de uitvoer bekijkt en controleert of die overeenkomt met wat de opgave vraagt.
