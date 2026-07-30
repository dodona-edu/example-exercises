Welkom op Dodona! In Dodona werk je steeds binnen een cursus. Een lesgever vult de cursus met **activiteiten**, gebundeld in reeksen. Er bestaan twee soorten activiteiten: leesactiviteiten en programmeeroefeningen.

### Waar je zit

Een reeks ziet er zo uit:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/01-series-nl-light.png" width="966" alt="Een reeks met een leesactiviteit en een oefening, met statusicoontjes">
  <img class="dark-only" src="media/01-series-nl-dark.png" width="966" alt="Een reeks met een leesactiviteit en een oefening, met statusicoontjes">
</div>

Een reeks heeft een titel, een korte beschrijving, soms een deadline, en daaronder de lijst met activiteiten. Bij elke activiteit staat vooraan een vinkje zodra je ze afgerond hebt, daarnaast een icoontje voor de soort activiteit, en rechts je status in woorden.

### Deze pagina is een leesactiviteit

Een leesactiviteit is tekst: een uitleg, een voorbeeld, een stukje theorie. Er is geen editor en er valt niets in te dienen. Als je ze gelezen hebt, klik je op de knop onderaan de pagina:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/02-mark-as-read-nl-light.png" width="1077" alt="De knop Markeren als gelezen">
  <img class="dark-only" src="media/02-mark-as-read-nl-dark.png" width="1077" alt="De knop Markeren als gelezen">
</div>

De knop maakt dan plaats voor het moment waarop je dat deed, en de activiteit krijgt een vinkje in de reeks:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/03-read-at-nl-light.png" width="1077" alt="De tekst: Gelezen op een datum">
  <img class="dark-only" src="media/03-read-at-nl-dark.png" width="1077" alt="De tekst: Gelezen op een datum">
</div>

> Een pagina als gelezen markeren houdt enkel je voortgang bij, voor jou en voor de lesgever. Je kunt zo vaak terugkomen en herlezen als je wilt.
{: .callout.callout-info}

### Bij een oefening schrijf je code

Een programmeeroefening is de tweede soort activiteit. Onder de opgave krijg je een editor, en daar schrijf je je oplossing.

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/04-handin-nl-light.png" width="1077" alt="De editor met daaronder de knop Indienen">
  <img class="dark-only" src="media/04-handin-nl-dark.png" width="1077" alt="De editor met daaronder de knop Indienen">
</div>

1. In de editor staat soms al wat begincode. Je kunt die aanpassen, aanvullen of helemaal weghalen.
2. Bij Python-oefeningen kun je je code eerst in je browser uitproberen met **Naar sandbox**. Je dient dan nog niets in, dus experimenteer gerust.
3. Ben je tevreden? Klik op **Indienen**. Dodona voert je code uit tegen een reeks testen en toont je binnen enkele seconden het resultaat.

### De feedback lezen

Slaagt je code voor alle testen, dan krijg je een groene **Correct**:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/05-correct-nl-light.png" width="1045" alt="Feedback van een correcte oplossing: een groene Correct en een test die slaagt">
  <img class="dark-only" src="media/05-correct-nl-dark.png" width="1045" alt="Feedback van een correcte oplossing: een groene Correct en een test die slaagt">
</div>

Zo niet, dan krijg je een rode **Fout**, en toont Dodona welke test faalde en hoe jouw uitvoer verschilt van wat er verwacht werd:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/06-wrong-nl-light.png" width="1045" alt="Feedback van een foute oplossing, met jouw uitvoer naast de verwachte uitvoer">
  <img class="dark-only" src="media/06-wrong-nl-dark.png" width="1045" alt="Feedback van een foute oplossing, met jouw uitvoer naast de verwachte uitvoer">
</div>

Drie gewoontes maken die feedback interpreteren een stuk eenvoudiger:

- **Kijk eerst naar de test die faalde.** Daar staat wat er precies verkeerd ging. Het aantal bovenaan (`0/1 correct`) zegt alleen hoeveel testen geslaagd zijn, niet wat je moet aanpassen.
- **Vergelijk de twee kolommen.** Links staat jouw uitvoer, rechts de verwachte uitvoer, en de tekens die verschillen zijn gemarkeerd. Let op de kleine dingen: een hoofdletter, een komma, een spatie op het einde van een regel.
- **Pas één ding aan en dien opnieuw in.** Vijf dingen tegelijk veranderen maakt het moeilijk om te zien wat geholpen heeft.

Het oordeel bovenaan de feedback is een van deze:

<div class="dodona-centered-group">
  <table class="table table-condensed">
    <thead>
      <tr style="background-color: var(--d-code-bg);">
        <th></th>
        <th>Oordeel</th>
        <th>Wat het betekent</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><i class="mdi mdi-check mdi-18 colored-correct" aria-hidden="true"></i></td>
        <td>Correct</td>
        <td>Alle testen slaagden.</td>
      </tr>
      <tr>
        <td><i class="mdi mdi-close mdi-18 colored-wrong" aria-hidden="true"></i></td>
        <td>Fout</td>
        <td>Je code liep, maar minstens één test gaf niet het verwachte resultaat.</td>
      </tr>
      <tr>
        <td><i class="mdi mdi-flash mdi-18 colored-wrong" aria-hidden="true"></i></td>
        <td>Uitvoeringsfout</td>
        <td>Je code crashte tijdens het uitvoeren. De foutmelding staat in de feedback.</td>
      </tr>
      <tr>
        <td><i class="mdi mdi-lightning-bolt-circle mdi-18 colored-wrong" aria-hidden="true"></i></td>
        <td>Compilatiefout</td>
        <td>Je code kon niet gelezen worden, meestal een typfout of een syntaxfout.</td>
      </tr>
      <tr>
        <td><i class="mdi mdi-alarm mdi-18 colored-wrong" aria-hidden="true"></i></td>
        <td>Timeout</td>
        <td>Je code deed er te lang over, vaak door een lus die nooit stopt.</td>
      </tr>
    </tbody>
  </table>
</div>

### Opmerkingen van de lesgever

De testen zijn automatisch, maar de lesgever kan je code ook zelf nalezen en opmerkingen bij bepaalde regels achterlaten. Die verschijnen bij je ingediende oplossing, onder het tabblad **Code**:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/08-annotation-nl-light.png" width="1045" alt="Een opmerking van de lesgever bij een regel code">
  <img class="dark-only" src="media/08-annotation-nl-dark.png" width="1045" alt="Een opmerking van de lesgever bij een regel code">
</div>

Je kunt er meteen onder antwoorden, dus zo'n opmerking is het begin van een gesprek en niet het laatste woord.

### Opnieuw indienen kost niets

Je mag zo vaak indienen als je wilt. Elke poging wordt bijgehouden en je kunt de oude terug openen via je ingediende oplossingen, dus niets van wat je probeerde gaat verloren:

<div class="dodona-centered-group dodona-shot">
  <img class="light-only" src="media/07-history-nl-light.png" width="351" alt="De lijst met ingediende oplossingen, met een foute en een correcte oplossing">
  <img class="dark-only" src="media/07-history-nl-dark.png" width="351" alt="De lijst met ingediende oplossingen, met een foute en een correcte oplossing">
</div>

Enkel je laatste oplossing telt, dus een foute poging kost je niets.

### Nu jij

Dat is alles wat je moet weten. Zette de lesgever de oefening **Je eerste oplossing** hierna in deze reeks? Open ze dan nu: de oplossing staat al voor je klaar, dus je hoeft enkel op **Indienen** te klikken en te kijken hoe de feedback verschijnt.

En als je klaar bent met lezen: klik hieronder op **Markeren als gelezen**.

<style>
  .dodona-shot img {
    max-width: 100%;
    height: auto;
  }
</style>
