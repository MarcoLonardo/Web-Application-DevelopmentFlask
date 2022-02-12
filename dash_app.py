# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
import plotly.validators.layout.colorscale
from dash import dash, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import html
import plotly_express as px
import plotly.graph_objs as go
import plotly.io as pio
pio.renderers.default = "notebook"
from pathlib import Path
from dash import dcc, Input, Output

# Reading the cleaned and prepared dataset from the Data directory
file_path = Path(__file__).parent.joinpath('Data','prepared_dataset.csv')
df_country = pd.read_csv(file_path)

# Addressing Question 1: Creating a Dataframe to group overall performance by country
df = df_country.groupby(['Country Name','Country Code',
                        ])[['Overall Score']].mean()
df.reset_index(inplace=True)
print(df[:5])

# Plotting the results with a choropleth graph
fig_bar = px.bar(df_country, x="Country Name", y="Year", title="Overall Business Performance")
fig = px.choropleth(
    data_frame=df,
    locations='Country Code',
    color="Overall Score",
    range_color=(75,85),
    scope="europe",
    color_continuous_scale=px.colors.diverging.RdYlGn,
    hover_name="Country Name"
    )

# Updating the layout and hiding countries not politically involved in the EU
fig.update_layout(height=650, width=900)
fig.update_geos(fitbounds="locations", visible=False)


external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
# Row 1 for title (column 1) and logo (column 2)
dbc.Row(dbc.Col(html.P(""))),
    dbc.Row([
        # This is for the London area selector and the statistics panel.
        dbc.Col(width=10, children=[
            html.H1('Europe Data Platform'),
            html.H1('Doing Business Performance'),

        ]),
        # Add the second column here. This is for the figure.
        dbc.Col(width=2,  children=[
            html.Img(src="https://upload.wikimedia.org/wikipedia/commons/8/84/European_Commission.svg",
                     alt="EU Commission Logo", width=150, height=100)
        ])
    ]),

# Rpw 2 for graph and panel

    dbc.Row(dbc.Col(html.P(""))),
    dbc.Row([
        # This is for the London area selector and the statistics panel.
        dbc.Col(width=3, children=[
            dcc.Dropdown(id="select_year",
                         options=[
                             {"label":"2015","value":2015},
                             {"label":"2016","value":2016},
                             {"label":"2017","value":2017},
                             {"label":"2018","value":2018},
                             {"label":"2019","value":2019},
                             {"label":"2020","value":2020}],
                             multi=False,
                             value=2020,
                         style={'width':'103%'}),
            # Div that will later contain a bootstrap card format showing the stats.
            html.Br(),
            html.Div(id="stats-card")



        ]),
        # Add the second column here. This is for the figure.
        dbc.Col(width=9,  children=[
            dcc.Graph(
                id='overall_score_chart',
                figure=fig)
        ])
    ])
])


@app.callback(
    [Output(component_id='stats-card', component_property='children'),
     Output(component_id='overall_score_chart', component_property='figure')],
    [Input(component_id='select_year', component_property='value')]
)

def update_graph (option_selected):
    print(option_selected)
    print(type(option_selected))

    container = " Year selected: {}".format(option_selected)

    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)
