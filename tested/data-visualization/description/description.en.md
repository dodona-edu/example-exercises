Pokémon trainers love data almost as much as they love their team. In this exercise you'll analyse a CSV file of Pokémon stats with [pandas](https://pandas.pydata.org/) and visualise the strongest ones with [matplotlib](https://matplotlib.org/).

You receive four CSV files in your working directory. Each row describes one Pokémon with the following columns:

<div class="dodona-centered-group">
<table class="table table-striped table-condensed">
  <thead>
    <tr><th>Column</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><code>name</code></td><td>Name of the Pokémon</td></tr>
    <tr><td><code>type1</code></td><td>Primary type (e.g. <code>Fire</code>, <code>Water</code>, <code>Grass</code>)</td></tr>
    <tr><td><code>type2</code></td><td>Secondary type, may be empty</td></tr>
    <tr><td><code>hp</code></td><td>Hit points</td></tr>
    <tr><td><code>attack</code></td><td>Physical attack</td></tr>
    <tr><td><code>defense</code></td><td>Physical defense</td></tr>
    <tr><td><code>sp_attack</code></td><td>Special attack</td></tr>
    <tr><td><code>sp_defense</code></td><td>Special defense</td></tr>
    <tr><td><code>speed</code></td><td>Speed</td></tr>
  </tbody>
</table>
</div>

The **total stats** of a Pokémon are the sum of its six numeric stats (`hp + attack + defense + sp_attack + sp_defense + speed`).

The four files are:

- [`pokemon.csv`](media/pokemon.csv) — 20 Pokémon from various types
- [`starters.csv`](media/starters.csv) — the nine Generation 1 starter evolutions
- [`eeveelutions.csv`](media/eeveelutions.csv) — Eevee and three of its evolutions
- [`legendary.csv`](media/legendary.csv) — just one legendary Pokémon

### Functions to write

The editor is pre-filled with stubs for every function you have to implement and a small `__main__` block that calls them on `pokemon.csv` and shows the chart. Replace each `raise NotImplementedError` with your implementation — pressing **Run** then prints the textual results and renders the bar chart in the sandbox.

You may import `pandas` and `matplotlib.pyplot`.

#### `load_pokemon(filename)`

Read the given CSV file and return the resulting `pandas.DataFrame`. The other functions can rely on this helper.

#### `number_of_pokemon(filename)`

Return the number of Pokémon in the file (an `int`).

```console?lang=python&prompt=>>>
>>> number_of_pokemon('pokemon.csv')
20
>>> number_of_pokemon('legendary.csv')
1
```

#### `all_types(filename)`

Return the **sorted** list of unique primary types (`type1`) that occur in the file.

```console?lang=python&prompt=>>>
>>> all_types('starters.csv')
['Fire', 'Grass', 'Water']
>>> all_types('legendary.csv')
['Psychic']
```

#### `strongest_pokemon(filename)`

Return the name of the Pokémon with the highest total stats. When several Pokémon are tied for the highest total, return the one that appears first in the file.

```console?lang=python&prompt=>>>
>>> strongest_pokemon('pokemon.csv')
'Mewtwo'
>>> strongest_pokemon('starters.csv')
'Charizard'
```

#### `strongest_per_type(filename)`

Return a dictionary that maps each primary type to the name of its strongest Pokémon (the one with the highest total stats within that type). When several Pokémon of the same type are tied for the highest total, take the one that appears first in the file.

```console?lang=python&prompt=>>>
>>> strongest_per_type('starters.csv')
{'Fire': 'Charizard', 'Grass': 'Venusaur', 'Water': 'Blastoise'}
```

#### `plot_top_pokemon(filename, n)`

Build a matplotlib bar chart of the top `n` Pokémon by total stats (highest first) and return the resulting `Figure`. Each bar's label is the Pokémon name and its height is the total stats. The chart must have:

- title `Top {n} Pokémon by total stats` (with `{n}` filled in)
- x-axis label `Pokémon`
- y-axis label `Total stats`

```python
import matplotlib.pyplot as plt

fig = plot_top_pokemon('starters.csv', 3)
plt.show()  # shows the chart
```

The bars must appear sorted from highest to lowest total — when several Pokémon are tied, those that appear first in the file go first.
