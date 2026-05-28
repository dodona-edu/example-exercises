Pokémontrainers zijn bijna even gek op data als op hun team. In deze oefening analyseer je een CSV-bestand met Pokémon-statistieken met behulp van [pandas](https://pandas.pydata.org/) en visualiseer je de sterkste Pokémon met [matplotlib](https://matplotlib.org/).

In je werkmap staan vier CSV-bestanden. Elke rij beschrijft één Pokémon met de volgende kolommen:

<div class="dodona-centered-group">
<table class="table table-striped table-condensed">
  <thead>
    <tr><th>Kolom</th><th>Beschrijving</th></tr>
  </thead>
  <tbody>
    <tr><td><code>name</code></td><td>Naam van de Pokémon</td></tr>
    <tr><td><code>type1</code></td><td>Primair type (bv. <code>Fire</code>, <code>Water</code>, <code>Grass</code>)</td></tr>
    <tr><td><code>type2</code></td><td>Secundair type, mag leeg zijn</td></tr>
    <tr><td><code>hp</code></td><td>Levenspunten</td></tr>
    <tr><td><code>attack</code></td><td>Fysieke aanval</td></tr>
    <tr><td><code>defense</code></td><td>Fysieke verdediging</td></tr>
    <tr><td><code>sp_attack</code></td><td>Speciale aanval</td></tr>
    <tr><td><code>sp_defense</code></td><td>Speciale verdediging</td></tr>
    <tr><td><code>speed</code></td><td>Snelheid</td></tr>
  </tbody>
</table>
</div>

De **totale stats** van een Pokémon zijn de som van de zes numerieke waarden (`hp + attack + defense + sp_attack + sp_defense + speed`).

De vier bestanden zijn:

- `pokemon.csv` — 20 Pokémon van verschillende types
- `starters.csv` — de negen starter-evoluties uit Generatie 1
- `eeveelutions.csv` — Eevee en drie van haar evoluties
- `legendary.csv` — één enkele legendarische Pokémon

Ze staan al klaar in je sandbox, dus je kan ze rechtstreeks bij naam inlezen.

### Te schrijven functies

In de editor staan reeds stubs voor elke functie die je moet implementeren, gevolgd door een klein `__main__`-blok dat ze oproept op `pokemon.csv` en de grafiek toont. Vervang elke `raise NotImplementedError` door je eigen implementatie — als je dan op **Run** klikt, zie je de tekstuele resultaten en wordt de staafgrafiek in de sandbox getekend.

Je mag `pandas` en `matplotlib.pyplot` importeren.

#### `load_pokemon(filename)`

Lees het opgegeven CSV-bestand in en geef de resulterende `pandas.DataFrame` terug. De andere functies mogen op deze hulpfunctie steunen.

#### `number_of_pokemon(filename)`

Geeft het aantal Pokémon in het bestand terug (een `int`).

```console?lang=python&prompt=>>>
>>> number_of_pokemon('pokemon.csv')
20
>>> number_of_pokemon('legendary.csv')
1
```

#### `all_types(filename)`

Geeft de **gesorteerde** lijst terug met unieke primaire types (`type1`) die in het bestand voorkomen.

```console?lang=python&prompt=>>>
>>> all_types('starters.csv')
['Fire', 'Grass', 'Water']
>>> all_types('legendary.csv')
['Psychic']
```

#### `strongest_pokemon(filename)`

Geeft de naam terug van de Pokémon met de hoogste totale stats. Als meerdere Pokémon dezelfde hoogste totale stats hebben, geef dan diegene terug die eerst in het bestand voorkomt.

```console?lang=python&prompt=>>>
>>> strongest_pokemon('pokemon.csv')
'Mewtwo'
>>> strongest_pokemon('starters.csv')
'Charizard'
```

#### `strongest_per_type(filename)`

Geeft een dictionary terug die elk primair type koppelt aan de naam van de sterkste Pokémon van dat type (degene met de hoogste totale stats binnen dat type). Bij gelijke totalen binnen één type kies je de Pokémon die eerst in het bestand voorkomt.

```console?lang=python&prompt=>>>
>>> strongest_per_type('starters.csv')
{'Fire': 'Charizard', 'Grass': 'Venusaur', 'Water': 'Blastoise'}
```

#### `plot_top_pokemon(filename, n)`

Bouw een matplotlib-staafdiagram van de top `n` Pokémon op basis van totale stats (hoogste eerst) en geef de resulterende `Figure` terug. Het label van elke staaf is de naam van de Pokémon, de hoogte is de totale stats. Het diagram moet de volgende eigenschappen hebben:

- titel `Top {n} Pokémon by total stats` (met `{n}` ingevuld)
- label van de x-as: `Pokémon`
- label van de y-as: `Total stats`

```python
import matplotlib.pyplot as plt

fig = plot_top_pokemon('starters.csv', 3)
plt.show()  # toont de grafiek
```

De staven moeten gesorteerd zijn van hoogste naar laagste totale stats — bij ex aequo komen Pokémon die eerst in het bestand staan eerst.
