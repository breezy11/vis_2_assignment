from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import base64

app = Dash(__name__)

seeds_orderings = [[1, 0, 5, 4, 6, 2, 3], [4, 2, 0, 1, 3, 5, 6]]
seeds_groups = ['Kama', 'Rosa', 'Canadian']
tds_seeds = [0.434, 0.402]

cars_orderings = [[0, 2, 6, 1, 4, 5, 3, 7, 8], [1, 3, 0, 2, 5, 6, 4, 7, 8]]
cars_groups = ['US', 'Europe', 'Japan']
tds_cars = [0.678, 0.590]

glass_orderings = [[3, 8, 1, 4, 5, 6, 0, 2, 7, 9], [2, 0, 7, 6, 3, 4, 1, 8, 5, 9]]
glass_groups = ['building_windows_float_processed', 'building_windows_non_float_processed', 'vehicle_windows_float_processed', 'containers', 'tableware', 'headlamps']
tds_glass = [1.602, 1.473]

# App layout
app.layout = html.Div(children=[
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Cars', 'value': 'Cars'},
            {'label': 'Glass', 'value': 'Glass'},
            {'label': 'Seeds', 'value': 'Seeds'}
        ],
        value='Seeds'
    ),
    html.Div(children = [
        html.H3(id = 'ordering_output'),
        html.H4(id = 'class_1'),
        html.Div(children = [
            html.Img(id = "best_1", src="assets/seeds_best_1.png"),
            html.Img(id = "worst_1", src="assets/seeds_worst_1.png")
            ]),
        html.H4(id = 'class_2'),
        html.Div(children = [
            html.Img(id = "best_2", src="assets/seeds_best_2.png"),
            html.Img(id = "worst_2", src="assets/seeds_worst_2.png")
            ]),
        html.H4(id = 'class_3'),
        html.Div(children = [
            html.Img(id = "best_3", src="assets/seeds_best_3.png"),
            html.Img(id = "worst_3", src="assets/seeds_worst_3.png")
            ])
    ], style={'textAlign': 'center'}),
    html.Div(id="flexible_div")
])

@app.callback(
    [Output('best_1', 'src'), Output('worst_1', 'src'), Output('best_2', 'src'), Output('worst_2', 'src'), Output('best_3', 'src'), Output('worst_3', 'src'), Output('flexible_div', 'children'), Output('ordering_output', 'children'),
     Output('class_1', 'children'), Output('class_2', 'children'), Output('class_3', 'children')],
    [Input('my-dropdown', 'value')]
)
def update_plots(selected_dataset):
    if selected_dataset == "Cars":
        best_1 = "assets/cars_best_1.png"
        worst_1 = "assets/cars_worst_1.png"
        best_2 = "assets/cars_best_2.png"
        worst_2 = "assets/cars_worst_2.png"
        best_3 = "assets/cars_best_3.png"
        worst_3 = "assets/cars_worst_3.png"
        best_ordering = cars_orderings[0]
        worst_ordering = cars_orderings[1]
        tds = tds_cars
        groups = cars_groups
        div_return = html.Div()
    elif selected_dataset == "Seeds":
        best_1 = "assets/seeds_best_1.png"
        worst_1 = "assets/seeds_worst_1.png"
        best_2 = "assets/seeds_best_2.png"
        worst_2 = "assets/seeds_worst_2.png"
        best_3 = "assets/seeds_best_3.png"
        worst_3 = "assets/seeds_worst_3.png"
        best_ordering = seeds_orderings[0]
        worst_ordering = seeds_orderings[1]
        tds = tds_seeds
        groups = seeds_groups
        div_return = html.Div()
    elif selected_dataset == "Glass":
        best_1 = "assets/glass_best_1.png"
        worst_1 = "assets/glass_worst_1.png"
        best_2 = "assets/glass_best_2.png"
        worst_2 = "assets/glass_worst_2.png"
        best_3 = "assets/glass_best_3.png"
        worst_3 = "assets/glass_worst_3.png"
        best_ordering = glass_orderings[0]
        worst_ordering = glass_orderings[1]
        tds = tds_glass
        groups = glass_groups

        div_return = html.Div(children = [
            html.Div(children = [
                html.H4("Class: " + str(groups[3])),
                html.Img(src="assets/glass_best_5.png"),
                html.Img(src="assets/glass_worst_5.png")
                ]),
            html.Div(children = [
                html.H4("Class: " + str(groups[4])),
                html.Img(src="assets/glass_best_6.png"),
                html.Img(src="assets/glass_worst_6.png")
                ]),
            html.Div(children = [
                html.H4("Class: " + str(groups[5])),
                html.Img(src="assets/glass_best_7.png"),
                html.Img(src="assets/glass_worst_7.png")
                ])
        ], style={'textAlign': 'center'})

    ordering_output = "Left - Best column ordering: "  + str(best_ordering) + ", Tds-score: " + str(tds[0]) + " | Worst column ordering: "  + str(worst_ordering) + ', "Tds-score": ' + str(tds[1]) + " - Right"
    class_1 = "Class: " + str(groups[0])
    class_2 = "Class: " + str(groups[1])
    class_3 = "Class: " + str(groups[2])

    return [best_1, worst_1, best_2, worst_2, best_3, worst_3, div_return, ordering_output, class_1, class_2, class_3]

if __name__ == '__main__':
    app.run_server(debug=True)

