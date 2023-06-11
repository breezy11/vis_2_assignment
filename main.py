from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__)

# import seeds
seeds_1_best = pd.read_csv("results/seeds/orderings-data-sets/seeds_1_best.csv", index_col=0)
seeds_2_best = pd.read_csv("results/seeds/orderings-data-sets/seeds_2_best.csv", index_col=0)
seeds_3_best = pd.read_csv("results/seeds/orderings-data-sets/seeds_3_best.csv", index_col=0)
seeds_1_worst = pd.read_csv("results/seeds/orderings-data-sets/seeds_1_worst.csv", index_col=0)
seeds_2_worst = pd.read_csv("results/seeds/orderings-data-sets/seeds_2_worst.csv", index_col=0)
seeds_3_worst = pd.read_csv("results/seeds/orderings-data-sets/seeds_3_worst.csv", index_col=0)

seeds_best = [seeds_1_best, seeds_2_best, seeds_3_best]
seeds_worst = [seeds_1_worst, seeds_2_worst, seeds_3_worst]
seeds_dimensions = [seeds_1_best.columns.tolist(), seeds_1_worst.columns.tolist()]
seeds_orderings = [[1, 0, 5, 4, 6, 2, 3], [4, 2, 0, 1, 3, 5, 6]]
seeds_groups = ['Kama', 'Rosa', 'Canadian']
tds_seeds = [0.434, 0.402]

# import cars
cars_1_best = pd.read_csv("results/cars/orderings-data-sets/cars_1_best.csv", index_col=0)
cars_2_best = pd.read_csv("results/cars/orderings-data-sets/cars_2_best.csv", index_col=0)
cars_3_best = pd.read_csv("results/cars/orderings-data-sets/cars_3_best.csv", index_col=0)
cars_1_worst = pd.read_csv("results/cars/orderings-data-sets/cars_1_worst.csv", index_col=0)
cars_2_worst = pd.read_csv("results/cars/orderings-data-sets/cars_2_worst.csv", index_col=0)
cars_3_worst = pd.read_csv("results/cars/orderings-data-sets/cars_3_worst.csv", index_col=0)

cars_best = [cars_1_best, cars_2_best, cars_3_best]
cars_worst = [cars_1_worst, cars_2_worst, cars_3_worst]
cars_dimensions = [cars_1_best.columns.tolist(), cars_1_worst.columns.tolist()]
cars_orderings = [[0, 2, 6, 1, 4, 5, 3, 7, 8], [1, 3, 0, 2, 5, 6, 4, 7, 8]]
cars_groups = ['US', 'Europe', 'Japan']
tds_cars = [0.678, 0.590]

glass_1_best = pd.read_csv("results/glass/orderings-data-sets/glass_1_best.csv", index_col=0)
glass_2_best = pd.read_csv("results/glass/orderings-data-sets/glass_2_best.csv", index_col=0)
glass_3_best = pd.read_csv("results/glass/orderings-data-sets/glass_3_best.csv", index_col=0)
glass_5_best = pd.read_csv("results/glass/orderings-data-sets/glass_5_best.csv", index_col=0)
glass_6_best = pd.read_csv("results/glass/orderings-data-sets/glass_6_best.csv", index_col=0)
glass_7_best = pd.read_csv("results/glass/orderings-data-sets/glass_7_best.csv", index_col=0)

glass_1_worst = pd.read_csv("results/glass/orderings-data-sets/glass_1_worst.csv", index_col=0)
glass_2_worst = pd.read_csv("results/glass/orderings-data-sets/glass_2_worst.csv", index_col=0)
glass_3_worst = pd.read_csv("results/glass/orderings-data-sets/glass_3_worst.csv", index_col=0)
glass_5_worst = pd.read_csv("results/glass/orderings-data-sets/glass_5_worst.csv", index_col=0)
glass_6_worst = pd.read_csv("results/glass/orderings-data-sets/glass_6_worst.csv", index_col=0)
glass_7_worst = pd.read_csv("results/glass/orderings-data-sets/glass_7_worst.csv", index_col=0)

glass_best = [glass_1_best, glass_2_best, glass_3_best, glass_5_best, glass_6_best, glass_7_best]
glass_worst = [glass_1_worst, glass_2_worst, glass_3_worst, glass_5_worst, glass_6_worst, glass_7_worst]
glass_dimensions = [glass_1_best.columns.tolist(), glass_1_worst.columns.tolist()]
glass_orderings = [[3, 8, 1, 4, 5, 6, 0, 2, 7, 9], [2, 0, 7, 6, 3, 4, 1, 8, 5, 9]]
glass_groups = ['building_windows_float_processed', 'building_windows_non_float_processed', 'vehicle_windows_float_processed', 'containers', 'tableware', 'headlamps']
tds_glass = [1.602, 1.473]

# Create parallel coordinate plots
fig_1_best = px.parallel_coordinates(seeds_1_best, dimensions=seeds_dimensions[0],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_2_best = px.parallel_coordinates(seeds_2_best, dimensions=seeds_dimensions[0],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_3_best = px.parallel_coordinates(seeds_3_best, dimensions=seeds_dimensions[0],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_1_worst = px.parallel_coordinates(seeds_1_worst, dimensions=seeds_dimensions[1],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_2_worst = px.parallel_coordinates(seeds_2_worst, dimensions=seeds_dimensions[1],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

fig_3_worst = px.parallel_coordinates(seeds_3_worst, dimensions=seeds_dimensions[1],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

# App layout
app.layout = html.Div(children = [
    html.H2(
            children='Reordering Sets of Parallel Coordinates Plots to Highlight Differences in Clusters',
            style={'textAlign': 'center'}
    ),
    html.Div([
    html.H4(children = 'Select the data set', style={'textAlign': 'center'}),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Cars', 'value': 'Cars'},
            {'label': 'Glass', 'value': 'Glass'},
            {'label': 'Seeds', 'value': 'Seeds'}
        ],
        value='Seeds'  # Default selected value
    )
    ]),
    html.Div(children = [
        html.Div(children = [
            html.H3(
            id = 'ordering_output'),
            ], style={'textAlign': 'center'}),
        html.Div(children = [
            html.H4(id = 'class_1'),
            dcc.Graph(
                id = 'pcp_1_best',
                figure = fig_1_best,
                style={'display': 'inline-block'}
                ),
            dcc.Graph(
                id = 'pcp_1_worst',
                figure = fig_1_worst,
                style={'display': 'inline-block'}
                )
            ], style={'textAlign': 'center'}),
        html.Div(children = [
            html.H4(id = 'class_2'),
            dcc.Graph(
                id = 'pcp_2_best',
                figure = fig_2_best,
                style={'display': 'inline-block'}
                ),
            dcc.Graph(
                id = 'pcp_2_worst',
                figure = fig_2_worst,
                style={'display': 'inline-block'}
                )
            ], style={'textAlign': 'center'}),
        html.Div(children = [
            html.H4(id = 'class_3'),
            dcc.Graph(
                id = 'pcp_3_best',
                figure = fig_3_best,
                style={'display': 'inline-block'}
                ),
            dcc.Graph(
                id = 'pcp_3_worst',
                figure = fig_3_worst,
                style={'display': 'inline-block'}
                )
            ], style={'textAlign': 'center'}),
        html.Div(id="flexible_div"),
        ])
    ])

@app.callback(
    [Output('pcp_1_best', 'figure'),
     Output('pcp_2_best', 'figure'),
     Output('pcp_3_best', 'figure'),
     Output('pcp_1_worst', 'figure'),
     Output('pcp_2_worst', 'figure'),
     Output('pcp_3_worst', 'figure'),
     Output('ordering_output', 'children'),
     Output('flexible_div', 'children'), Output('class_1', 'children'), Output('class_2', 'children'), Output('class_3', 'children')],
    [Input('my-dropdown', 'value')]
)
def update_plots(selected_dataset):

    if selected_dataset == 'Seeds':
        best_1 = seeds_1_best
        best_2 = seeds_2_best
        best_3 = seeds_3_best
        worst_1 = seeds_1_worst
        worst_2 = seeds_2_worst
        worst_3 = seeds_3_worst
        dimensions = seeds_dimensions
        groups = seeds_groups
        best_ordering = seeds_orderings[0]
        worst_ordering = seeds_orderings[1]
        tds = tds_seeds
        div_return = html.Div()
    elif selected_dataset == 'Cars':
        best_1 = cars_1_best
        best_2 = cars_2_best
        best_3 = cars_3_best
        worst_1 = cars_1_worst
        worst_2 = cars_2_worst
        worst_3 = cars_3_worst
        dimensions = cars_dimensions
        groups = cars_groups
        best_ordering = cars_orderings[0]
        worst_ordering = cars_orderings[1]
        tds = tds_cars
        div_return = html.Div()
    elif selected_dataset == 'Glass':
        best_1 = glass_1_best
        best_2 = glass_2_best
        best_3 = glass_3_best
        worst_1 = glass_1_worst
        worst_2 = glass_2_worst
        worst_3 = glass_3_worst
        dimensions = glass_dimensions
        groups = glass_groups
        best_ordering = glass_orderings[0]
        worst_ordering = glass_orderings[1]
        tds = tds_glass

        fig_5_best = px.parallel_coordinates(glass_5_best, dimensions=glass_dimensions[0],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)

        fig_6_best = px.parallel_coordinates(glass_6_best, dimensions=glass_dimensions[0],
                                       color_continuous_scale=px.colors.diverging.Tealrose,
                                       color_continuous_midpoint=2)

        fig_7_best = px.parallel_coordinates(glass_7_best, dimensions=glass_dimensions[0],
                                       color_continuous_scale=px.colors.diverging.Tealrose,
                                       color_continuous_midpoint=2)

        fig_5_worst = px.parallel_coordinates(glass_5_worst, dimensions=glass_dimensions[1],
                                       color_continuous_scale=px.colors.diverging.Tealrose,
                                       color_continuous_midpoint=2)

        fig_6_worst = px.parallel_coordinates(glass_6_worst, dimensions=glass_dimensions[1],
                                       color_continuous_scale=px.colors.diverging.Tealrose,
                                       color_continuous_midpoint=2)

        fig_7_worst = px.parallel_coordinates(glass_7_worst, dimensions=glass_dimensions[1],
                               color_continuous_scale=px.colors.diverging.Tealrose,
                               color_continuous_midpoint=2)


        div_return = html.Div(children = [
            html.Div(children = [
                html.H4(
                'Class = ' + str(groups[3])
                ),
                dcc.Graph(
                    figure = fig_5_best,
                    style={'display': 'inline-block'}
                    ),
                dcc.Graph(  
                    figure = fig_5_worst,
                    style={'display': 'inline-block'}
                    )
                ], style={'textAlign': 'center'}),
            html.Div(children = [
                html.H4(
                'Class = ' + str(groups[4])
                ),
                dcc.Graph(
                    figure = fig_6_best,
                    style={'display': 'inline-block'}
                    ),
                dcc.Graph(
                    figure = fig_6_worst,
                    style={'display': 'inline-block'}
                    )
                ], style={'textAlign': 'center'}),
            html.Div(children = [
                html.H4(
                'Class = ' + str(groups[5])
                ),
                dcc.Graph(
                    figure = fig_7_best,
                    style={'display': 'inline-block'}
                    ),
                dcc.Graph(
                    figure = fig_7_worst,
                    style={'display': 'inline-block'}
                    )
                ], style={'textAlign': 'center'})
        ])

    fig_1_best = px.parallel_coordinates(best_1, dimensions=dimensions[0],
                                         color_continuous_scale=px.colors.diverging.Tealrose,
                                         color_continuous_midpoint=2)
    fig_2_best = px.parallel_coordinates(best_2, dimensions=dimensions[0],
                                         color_continuous_scale=px.colors.diverging.Tealrose,
                                         color_continuous_midpoint=2)
    fig_3_best = px.parallel_coordinates(best_3, dimensions=dimensions[0],
                                         color_continuous_scale=px.colors.diverging.Tealrose,
                                         color_continuous_midpoint=2)

    fig_1_worst = px.parallel_coordinates(worst_1, dimensions=dimensions[1],
                                          color_continuous_scale=px.colors.diverging.Tealrose,
                                          color_continuous_midpoint=2)
    fig_2_worst = px.parallel_coordinates(worst_2, dimensions=dimensions[1],
                                          color_continuous_scale=px.colors.diverging.Tealrose,
                                          color_continuous_midpoint=2)
    fig_3_worst = px.parallel_coordinates(worst_3, dimensions=dimensions[1],
                                          color_continuous_scale=px.colors.diverging.Tealrose,
                                          color_continuous_midpoint=2)

    ordering_output = "Left - Best column ordering: "  + str(best_ordering) + ", Tds-score: " + str(tds[0]) + " | Worst column ordering: "  + str(worst_ordering) + ', "Tds-score": ' + str(tds[1]) + " - Right"

    class_1 = "Class: " + str(groups[0])
    class_2 = "Class: " + str(groups[1])
    class_3 = "Class: " + str(groups[2])

    return fig_1_best, fig_2_best, fig_3_best, fig_1_worst, fig_2_worst, fig_3_worst, ordering_output, div_return, class_1, class_2, class_3


if __name__ == '__main__':
    app.run_server(debug=True)

