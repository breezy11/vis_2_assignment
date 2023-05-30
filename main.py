from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)

seeds_1_best = pd.read_csv("results/seeds/orderings-data-sets/seeds_1_best.csv", index_col=0)
seeds_2_best = pd.read_csv("results/seeds/orderings-data-sets/seeds_2_best.csv", index_col=0)
seeds_3_best = pd.read_csv("results/seeds/orderings-data-sets/seeds_3_best.csv", index_col=0)
seeds_1_worst = pd.read_csv("results/seeds/orderings-data-sets/seeds_1_worst.csv", index_col=0)
seeds_2_worst = pd.read_csv("results/seeds/orderings-data-sets/seeds_2_worst.csv", index_col=0)
seeds_3_worst = pd.read_csv("results/seeds/orderings-data-sets/seeds_3_worst.csv", index_col=0)

print(seeds_3_best.shape)

dimensions_1_best = seeds_1_best.columns
dimensions_1_worst = seeds_1_worst.columns

# Create parallel coordinate plots
fig_1_best = px.parallel_coordinates(seeds_1_best, dimensions=dimensions_1_best,
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_2_best = px.parallel_coordinates(seeds_2_best, dimensions=dimensions_1_best,
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_3_best = px.parallel_coordinates(seeds_3_best, dimensions=dimensions_1_best,
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_1_worst = px.parallel_coordinates(seeds_1_worst, dimensions=dimensions_1_worst,
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_2_worst = px.parallel_coordinates(seeds_2_worst, dimensions=dimensions_1_worst,
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_3_worst = px.parallel_coordinates(seeds_3_worst, dimensions=dimensions_1_worst,
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

# App layout
app.layout = html.Div(
    children=[
        html.H2(
            children='Reordering Sets of Parallel Coordinates Plots to Highlight Differences in Clusters',
            style={'textAlign': 'center'}
        ),
        html.H5(
            children='Best orderings: [1, 0, 5, 4, 6, 2, 3], Total Distance Score: 0.4345727485543593',
            style={'textAlign': 'center'}
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col",
                    children=[
                        dcc.Graph(
                            id='pcp_1_best',
                            figure=fig_1_best,
                            className='plot'
                        )
                    ]
                ),
                html.Div(
                    className="col",
                    children=[
                        dcc.Graph(
                            id='pcp_2_best',
                            figure=fig_2_best,
                            className='plot'
                        )
                    ]
                ),
                html.Div(
                    className="col",
                    children=[
                        dcc.Graph(
                            id='pcp_3_best',
                            figure=fig_3_best,
                            className='plot'
                        )
                    ]
                )
            ]
        ),
        html.H5(
            children='Worst orderings: [4, 2, 0, 1, 3, 5, 6], Total Distance Score: 0.401919672665923',
            style={'textAlign': 'center'}
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="col",
                    children=[
                        dcc.Graph(
                            id='pcp_1_worst',
                            figure=fig_1_worst,
                            className='plot'
                        )
                    ]
                ),
                html.Div(
                    className="col",
                    children=[
                        dcc.Graph(
                            id='pcp_2_worst',
                            figure=fig_2_worst,
                            className='plot'
                        )
                    ]
                ),
                html.Div(
                    className="col",
                    children=[
                        dcc.Graph(
                            id='pcp_3_worst',
                            figure=fig_3_worst,
                            className='plot'
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)


### code for changin the data sets
# Define the callback function
"""@app.callback(
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

,
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


"""