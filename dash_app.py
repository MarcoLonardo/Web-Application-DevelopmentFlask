# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.

from dash import dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html
import plotly_express as px
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = "notebook"
from pathlib import Path

file_path = Path(__file__).parent.joinpath('Data','cleaned_dataset.csv')
df_country = pd.read_csv(file_path)

fig_bar = px.bar(df_country, x="Country Name", y="2015", color="Indicator Name", title="Overall Busincess Performance", template="plotly_dark")


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.Img(src="https://upload.wikimedia.org/wikipedia/commons/8/84/European_Commission.svg",
             alt="EU Commission Logo"),
    html.H1(children='Europe Data Platform', style={'textAlign': 'center'}),
    html.H1(children='"Doing Business" Performance', style={'textAlign': 'center'}),

dcc.Graph(
    id='spend-bar-graph',
    figure=fig_bar
)
])



if __name__ == '__main__':
    app.run_server(debug=True)
