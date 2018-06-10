# Visualizing single Pokemon statistics
import plotly.graph_objs as go

# Defining colors for graphs
colors = {
    "Bug": "#A6B91A",
    "Dark": "#705746",
    "Dragon": "#6F35FC",
    "Electric": "#F7D02C",
    "Fairy": "#D685AD",
    "Fighting": "#C22E28",
    "Fire": "#EE8130",
    "Flying": "#A98FF3",
    "Ghost": "#735797",
    "Grass": "#7AC74C",
    "Ground": "#E2BF65",
    "Ice": "#96D9D6",
    "Normal": "#A8A77A",
    "Poison": "#A33EA1",
    "Psychic": "#F95587",
    "Rock": "#B6A136",
    "Steel": "#B7B7CE",
    "Water": "#6390F0",
}


def polar_pokemon_stats(pkmn_name, pokemon):
    pkmn = pokemon[pokemon.Name == pkmn_name]
    obj = go.Scatterpolar(
        r=[
            pkmn['HP'].values[0],
            pkmn['Attack'].values[0],
            pkmn['Defense'].values[0],
            pkmn['Sp. Atk'].values[0],
            pkmn['Sp. Def'].values[0],
            pkmn['Speed'].values[0],
            pkmn['HP'].values[0]
        ],
        theta=[
            'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'HP'
        ],
        fill='toself',
        marker=dict(
            color=colors[pkmn['Type 1'].values[0]]
        ),
        name=pkmn['Name'].values[0]
    )

    return obj


def plot_single_pokemon(name, pokemon):
    layout = go.Layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 250]
            )
        ),
        showlegend=False,
        title="Stats of {}".format(name),
        autosize=True,
        paper_bgcolor='#009688'
    )

    pokemon_figure = go.Figure(data=[polar_pokemon_stats(name, pokemon)], layout=layout)
    return pokemon_figure


# Comparing stats of 2 different pokemons

def compare_two_pokemon(pkmn_1_name, pkmn_2_name, pokemon):
    layout = go.Layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 250]
            )
        ),
        showlegend=True,
        title="{} vs. {}".format(pkmn_1_name, pkmn_2_name),
        autosize=True,
        paper_bgcolor='#009688'
    )

    pkmn_1 = polar_pokemon_stats(pkmn_1_name, pokemon)
    pkmn_2 = polar_pokemon_stats(pkmn_2_name, pokemon)

    compare_2_pokemon = go.Figure(data=[pkmn_1, pkmn_2], layout=layout)
    return compare_2_pokemon


# Visualizing stats of pokemon per type

def stats_by_type(type, pokemon):
    data = []
    stats_names = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

    particular_type = pokemon[pokemon['Type 1'] == type].reset_index(drop=True)
    for stat in stats_names:
        stat_line = go.Scatter(
            x=particular_type['Name'],
            y=particular_type[stat],
            name=stat,
            line=dict(
                width=3
            )
        )

        data.append(stat_line)

    layout = go.Layout(
        title="Stats of every Pokemon of {} type".format(type),
        autosize=True,
        xaxis=dict(
            title="{} Pokemon".format(type)
        ),
        yaxis=dict(
            title="Values"
        )
    )

    fig = go.Figure(data=data, layout=layout)
    return fig


# Visualizing number of pokemon per type across all generation.
def number_by_type(pokemon):
    types = (pokemon.groupby(['Type 1'])['#'].count())
    types_name = list(types.keys())

    data = go.Bar(
        x=types_name,
        y=types.values,
        marker=dict(
            color=list(colors.values())
        ),
        name="{}".format(types_name)
    )

    layout = go.Layout(
        title='Types',
        xaxis=dict(
            title='Type'
        ),
        yaxis=dict(
            title='Number of Pokemon'
        )
    )

    fig = go.Figure(data=[data], layout=layout)
    return fig
