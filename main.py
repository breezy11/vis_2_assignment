#to see visualization use: http://127.0.0.1:8050/
from dash import Dash, dcc, html
import plotly.express as px
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as ply
import pandas as pd
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, ctx

app = Dash(__name__)

cars = pd.read_csv("data/cars/cars.csv",index_col=0)
ecoli = pd.read_csv("data/ecoli/ecoli.csv",index_col=0)
wine = pd.read_csv("data/wine/wine.csv",index_col=0)
glass = pd.read_csv("data/glass/glass.csv",index_col=0)
iris = pd.read_csv("data/iris/iris.csv",index_col=0)
seeds = pd.read_csv("data/seeds/seeds.csv",index_col=0)

datasets_names = ['cars', 'ecoli', 'wine', 'glass', 'iris', 'seeds']
datasets = [cars, ecoli, wine, glass, iris, seeds]

data_ = datasets[0]
dimensions = data_.columns

# parallel coordinate plot
fig = px.parallel_coordinates(data_, dimensions=dimensions,
                             color_continuous_scale=px.colors.diverging.Tealrose,
                             color_continuous_midpoint=2)
# app layout
app.layout = html.Div(
    children=[
        html.H2(
            children='Reordering Sets of Parallel Coordinates Plots to Highlight Differences in Clusters',
            style={'textAlign': 'center'}
        ),
        html.H6(
            children='Dario Jugo, Branimir Raguz',
            style={'textAlign': 'center'}
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id='parallel-coordinate',
                    figure=fig,
                    className='plot'
                )
            ]
        ),
        html.Div(
            children=[
                html.H3(
                    children='Select one of the datasets',
                    style={'textAlign': 'center'}
                ),
                dcc.Dropdown(
                    options=datasets_names,
                    value="cars",
                    multi=False,
                    id="dataset-selection"
                )
            ],
            style={'textAlign': 'center', 'margin': '20px'}
        )
    ]
)

# Define the callback function
@app.callback(
    Output('parallel-coordinate', 'figure'),
    Input('dataset-selection', 'value')
)
def update_parallel_coordinate(selected_dataset_name):
    # Get the selected dataset based on the dropdown value
    selected_dataset = datasets[datasets_names.index(selected_dataset_name)]
    dimensions = selected_dataset.columns

    # Create the updated parallel coordinate plot
    fig = px.parallel_coordinates(selected_dataset, dimensions=dimensions,
                                  color_continuous_scale=px.colors.diverging.Tealrose,
                                  color_continuous_midpoint=2)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)