import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import pokemon_plots

pokemon = pd.read_csv('https://raw.githubusercontent.com/lakshyaagrwal/pokemon_visualization/master/Pokemon.csv')

names = pokemon['Name'].unique()
types = pokemon['Type 1'].unique()

app = dash.Dash(__name__)
server = app.server

app.title = 'Pokemon Data Visualization'

app.layout = html.Div(className='container', children=[
    html.Div(className='col s12 teal hoverable z-index-3', children=[
        html.Div(className='row', children=[
            html.Div(className='col s6', children=[
                html.Label('Enter Pokemon #1', style={'color': 'white'}),
                dcc.Dropdown(
                    id='name-1',
                    options=[{'label': name, 'value': name} for name in names],
                    value='Bulbasaur',
                )]),
            html.Div(className='col s6', children=[
                html.Label('Enter Pokemon #2', style={'color': 'white'}),
                dcc.Dropdown(
                    id='name-2',
                    options=[{'label': name, 'value': name} for name in names],
                    value='Squirtle'
                )]),
        ]),

        html.Div(className='row', children=[
            html.Div(className='col s4 hoverable', children=[
                html.Div([
                    dcc.Graph(id='graph-1')
                ])
            ]),
            html.Div(className='col s4 hoverable', children=[
                html.Div([
                    dcc.Graph(id='graph-compare')
                ])
            ]),
            html.Div(className='col s4 hoverable', children=[
                html.Div([
                    dcc.Graph(id='graph-2')
                ])
            ])
        ])
    ]),

    html.Div(className='col s12', children=[
        html.Div(className='col s4', children=[
            html.Label('Select Type'),
            dcc.Dropdown(
                id='type-select',
                options=[{'label': type, 'value': type} for type in types],
                value='Fire',
            )
        ]),
        html.Div(className='col s8', children=[
            dcc.Graph(id='graph-type')
        ])
    ]),

    html.Div(className='col s12', children=[
        dcc.Graph(
            id='number_type',
            figure=pokemon_plots.number_by_type(pokemon)
        )
    ])
])


@app.callback(
    dash.dependencies.Output('graph-1', 'figure'),
    [dash.dependencies.Input('name-1', 'value')])
def update_graph_1(name):
    return pokemon_plots.plot_single_pokemon(name, pokemon)


@app.callback(
    dash.dependencies.Output('graph-2', 'figure'),
    [dash.dependencies.Input('name-2', 'value')])
def update_graph_2(name):
    return pokemon_plots.plot_single_pokemon(name, pokemon)


@app.callback(
    dash.dependencies.Output('graph-compare', 'figure'),
    [dash.dependencies.Input('name-1', 'value'),
     dash.dependencies.Input('name-2', 'value')], )
def update_compare_graph(name_1, name_2):
    return pokemon_plots.compare_two_pokemon(name_1, name_2, pokemon)


@app.callback(
    dash.dependencies.Output('graph-type', 'figure'),
    [dash.dependencies.Input('type-select', 'value')]
)
def update_type(type):
    return pokemon_plots.stats_by_type(type, pokemon)


app.css.append_css({
    "external_url": "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css"
})

app.scripts.append_script({
    "external_url": "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js"
})

app.scripts.append_script({
    "external_url": "https://rawgit.com/lakshyaagrwal/0d7d7547f4951bc772f5cfcb937b1ae7/"
                    "raw/02dad842082321b6fb2a69fc56d11d5cef6b7fef/init_material.js"
})

if __name__ == '__main__':
    app.run_server(debug=True)
