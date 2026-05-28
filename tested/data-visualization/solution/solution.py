import pandas as pd
import matplotlib.pyplot as plt

STATS = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']


def load_pokemon(filename):
    return pd.read_csv(filename)


def _with_total(df):
    df = df.copy()
    df['total'] = df[STATS].sum(axis=1)
    return df


def number_of_pokemon(filename):
    return len(load_pokemon(filename))


def all_types(filename):
    return sorted(load_pokemon(filename)['type1'].unique().tolist())


def strongest_pokemon(filename):
    df = _with_total(load_pokemon(filename))
    return df.loc[df['total'].idxmax(), 'name']


def strongest_per_type(filename):
    df = _with_total(load_pokemon(filename))
    idx = df.groupby('type1')['total'].idxmax()
    return {type_: df.loc[row, 'name'] for type_, row in idx.items()}


def plot_top_pokemon(filename, n):
    df = _with_total(load_pokemon(filename))
    top = df.nlargest(n, 'total')
    fig, ax = plt.subplots()
    ax.bar(top['name'], top['total'])
    ax.set_title(f"Top {n} Pokémon by total stats")
    ax.set_xlabel("Pokémon")
    ax.set_ylabel("Total stats")
    return fig


if __name__ == "sandbox":
    print("Number of Pokémon:", number_of_pokemon('pokemon.csv'))
    print("All types:        ", all_types('pokemon.csv'))
    print("Strongest:        ", strongest_pokemon('pokemon.csv'))
    print("Strongest per type:")
    for type_, name in strongest_per_type('pokemon.csv').items():
        print(f"  {type_:<10s} {name}")

    plot_top_pokemon('pokemon.csv', 5)
    plt.show()
