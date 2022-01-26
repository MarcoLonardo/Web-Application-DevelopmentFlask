# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
from dash import html

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Europe Data Platform'),

html.H1(children='"Doing Business" Performance'),


html.Img(
    src="https://upload.wikimedia.org/wikipedia/commons/8/84/European_Commission.svg",
    alt="EU Commission Logo"),

html.Table(
    [
        html.Tr([
            html.Td(children='row 1 col 1'),
            html.Td(children='row 1 col 2')
        ]),
        html.Tr([
            html.Td(children='row 2 col 1'),
            html.Td(children='row 2 col 2')
        ])
    ]
),
])


if __name__ == '__main__':
    app.run_server(debug=True)
