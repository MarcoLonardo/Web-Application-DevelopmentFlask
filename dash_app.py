from pathlib import Path
from dash import dcc, Input, Output
from dash import dash, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly_express as px
import plotly.io as pio

pio.renderers.default = "notebook"

# Reading and preparing the dataset for the choropleth (chart 1).
file_path = Path(__file__).parent.joinpath('Data', 'prepared_dataset.csv')
df_country = pd.read_csv(file_path)
df = df_country.groupby(['Year'])[['Getting Credit - Score', 'Resolving insolvency - Score',
                                   'Starting a business - Score', 'Trading across borders - Score',
                                   'Overall Score']].mean()
df.reset_index(inplace=True)
print(df[:5])

# Reading the second version of the prepared dataset with different data structure for the scatter map (chart 2)
file_path2 = Path(__file__).parent.joinpath('Data', 'prepared_dataset_v2.csv')
df_performance = pd.read_csv(file_path2)

# Removing irrelevant columns and duplicates from a new dataframe variable
df_overall = df_performance.copy()
df_overall = df_overall.drop('Indicator', 1)
df_overall = df_overall.drop('Score', 1)
df_overall = df_overall.drop_duplicates('Country Name')

# Reading the third version of the prepared dataset with different data structure for chart 3
file_path3 = Path(__file__).parent.joinpath('Data', 'prepared_dataset_v3.csv')
df1 = pd.read_csv(file_path3)

# Data Preparation for Icicle
df_icicle = df1.copy()
# Calculating the average 5-year performance
df_icicle = df_icicle.groupby('Country Name').mean().reset_index()
# Dropping the column year because the Overall Score refers to the 5-Year Avg Performance
df_icicle = df_icicle.drop('Year', 1)
# Creating a new column for the Icicle Root Node
df_icicle['Currency Unit'] = 'Europe'

fig3 = px.icicle(df_icicle, path=['Currency Unit', 'Country Name'], values="Score", color="Score",
                 color_continuous_scale='RdBu', custom_data=['Country Name'])

fig3.update_layout(
    uniformtext=dict(minsize=50), margin=dict(t=50, l=25, r=25, b=25))

external_stylesheets = [dbc.themes.LUX]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    # Row 1 for title (column 1) and logo (column 2)
    dbc.Row(dbc.Col(html.P(""))),
    dbc.Row([
        # Column 1 for the title.
        dbc.Col(width=10, children=[
            html.H1('Europe Data Platform'),
            html.H1('Doing Business Performance'),
        ]),
        # Column 2 for the logo
        dbc.Col(width=2, children=[
            html.Img(src="https://upload.wikimedia.org/wikipedia/commons/8/84/European_Commission.svg",
                     alt="EU Commission Logo", width=150, height=100)
        ])
    ]),

    # Row 2 for the statistics panel (column 1) and the choropleth (column 2)
    dbc.Row(dbc.Col(html.P(""))),
    dbc.Row([
        html.P('Which countries in Europe have, on average, performed worse in 2020 and in previous years?'),
        # Column1 for the statistic panel
        dbc.Col(width=3, children=[
            # Dropdown Selection Panel
            dcc.Dropdown(id="select_year",
                         options=[
                             {"label": "2016", "value": 2016},
                             {"label": "2017", "value": 2017},
                             {"label": "2018", "value": 2018},
                             {"label": "2019", "value": 2019},
                             {"label": "2020", "value": 2020}],
                         multi=False,
                         value=2020,
                         style={'width': '100%'}),
            # Stats Benchmarking Score Card
            html.Br(),
            html.Div(id="stats-card")

        ]),
        # Column 2 for the choropleth
        dbc.Col(width=9, children=[
            dcc.Graph(
                id='overall_score_chart',
                figure={})
        ]),

        # Row 3 for the Scatter Map and the drop-down menu
        dbc.Row(dbc.Col(html.P(""))),
        dbc.Row([
            html.P('What problems are each of the countries facing?'),
            # Dropdown Selection Filter
            dcc.Dropdown(id="select_country",
                         options=[
                             {"label": "Austria", "value": "Austria"},
                             {"label": "Belgium", "value": "Belgium"},
                             {"label": "Cyprus", "value": "Cyprus"},
                             {"label": "Estonia", "value": "Estonia"},
                             {"label": "Finland", "value": "Finland"},
                             {"label": "France", "value": "France"},
                             {"label": "Germany", "value": "Germany"},
                             {"label": "Greece", "value": "Greece"},
                             {"label": "Ireland", "value": "Ireland"},
                             {"label": "Italy", "value": "Italy"},
                             {"label": "Kosovo", "value": "Kosovo"},
                             {"label": "Latvia", "value": "Latvia"},
                             {"label": "Lithuania", "value": "Lithuania"},
                             {"label": "Luxembourg", "value": "Luxembourg"},
                             {"label": "Malta", "value": "Malta"},
                             {"label": "Montenegro", "value": "Montenegro"},
                             {"label": "Netherlands", "value": "Netherlands"},
                             {"label": "Portugal", "value": "Portugal"},
                             {"label": "Slovak Republic", "value": "Slovak Republic"},
                             {"label": "Slovenia", "value": "Slovenia"},
                             {"label": "Spain", "value": "Spain"}],
                         value=["Austria", "Belgium", "Cyprus", "Estonia", "Finland", "France", "Germany",
                                "Greece", "Ireland", "Ireland", "Italy", "Kosovo", "Latvia", "Lithuania",
                                "Luxembourg", "Malta", "Montenegro", "Netherlands", "Portugal",
                                "Slovak Republic", "Slovenia", "Slovenia", "Spain"],
                         multi=True,
                         searchable=True,
                         clearable=False,
                         placeholder="select one or multiple countries",
                         style={'width': '100%'}),
            html.Br(),
            html.Div(id="country_selection_panel", children=[]),
            # Scatter Map box
            dcc.Graph(
                id='scatter_indicator_chart',
                figure={}),

            # Row 4 for the Icicle Chart (Column 1) and the Line chart (Column 2)
            dbc.Row(dbc.Col(html.P(""))),
            dbc.Row([
                html.P(
                    'How has the performance of each country changed across the 4 indicators over the years?'),
                # Column 1 for Icicle filtering chart
                dbc.Col(width=3, children=[
                    dcc.Graph(id='icicle', figure=fig3, clickData=None, hoverData=None,
                              config={
                                  'staticPlot': False,  # True, False
                                  'scrollZoom': True,  # True, False
                                  'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                                  'showTips': False,  # True, False
                                  'displayModeBar': True,  # True, False, 'hover'
                                  'watermark': True,
                                  # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                              },
                              className='six columns'
                              ),

                ]),
                # Column to for the line chart
                dbc.Col(width=9, children=[
                    dcc.Graph(id='line_graph',
                              figure={}, className='six columns')
                ])
            ]),

        ])

    ])

])


@app.callback(
    [Output(component_id='stats-card', component_property='children'),
     Output(component_id='overall_score_chart', component_property='figure')],
    [Input(component_id='select_year', component_property='value')]
)
# Interactivity to the choropleth map and the stats card with selection
def update_on_selection(option_selected):
    df_filtering1 = df.copy()
    df_filtering1 = df_filtering1[df_filtering1["Year"] == option_selected]
    df_filtering1 = df_filtering1.round(decimals=1)
    card = dbc.Card(className="bg-dark text-light", children=[
        dbc.CardBody([
            html.H4(" Year selected: {}".format(option_selected), className="card-text text-light"),
            html.Br(),
            html.H6("Getting Credit Average:", className="card-title"),
            html.H4(df_filtering1['Getting Credit - Score'].tolist(), className="card-text text-light"),
            html.Br(),
            html.H6("Resolving insolvency Average:", className="card-title"),
            html.H4(df_filtering1['Resolving insolvency - Score'].tolist(), className="card-text text-light"),
            html.Br(),
            html.H6("Starting a business Average:", className="card-title"),
            html.H4(df_filtering1['Starting a business - Score'].tolist(), className="card-text text-light"),
            html.Br(),
            html.H6("Trading across borders Average:", className="card-title"),
            html.H4(df_filtering1['Trading across borders - Score'].tolist(), className="card-text text-light"),
            html.Br(),
            html.H6("Overall Average:", className="card-title"),
            html.H4(df_filtering1['Overall Score'].tolist(), className="card-text text-light"),
            html.Br()
        ])
    ])

    df_filtering = df_country.copy()
    df_filtering = df_filtering[df_filtering["Year"] == option_selected]

    # Plotting the results with a choropleth graph
    fig = px.choropleth(
        data_frame=df_filtering,
        locations='Country Code',
        color="Overall Score",
        range_color=(75, 85),
        scope="europe",
        color_continuous_scale=px.colors.diverging.BrBG,
        hover_name="Country Name"
    )

    # Updating the layout and hiding countries not politically involved in the EU
    fig.update_layout(height=650, width=900)
    fig.update_geos(fitbounds="locations", visible=True)

    return card, fig


@app.callback(
    [Output(component_id='country_selection_panel', component_property='children'),
     Output(component_id='scatter_indicator_chart', component_property='figure')],
    [Input(component_id='select_country', component_property='value')]
)
# Adding interactivity to the scatter map chart
def update_countries(country_selected):
    df_performance1 = df_performance[(df_performance["Country Name"].isin(country_selected))]

    container = "Selected: {}".format(country_selected)

    fig2 = px.scatter(df_performance1, x="Score", y="Overall Score", animation_frame="Year",
                      animation_group="Country Name",
                      size="Score", color="Indicator", hover_name="Country Name", facet_col="Indicator",
                      size_max=12, range_x=[0, 105], range_y=[0, 105])

    fig2.update_layout(height=650, width=1400)

    return container, fig2


@app.callback(
    Output(component_id='line_graph', component_property='figure'),
    Input(component_id='icicle', component_property='hoverData'),
)
# Interactivity to the the line chart: updating the line chart countries on hovering over the countries in the icicle
def update_line_graph(hov_data):
    if hov_data is None:
        dff = df1[df1["Country Name"] == "empty"]
        fig4 = px.line(dff, x='Year', y="Score", color="Indicator",
                       title='Business Performance <br><sup>Select a country on the left to display performance</sup>')
        return fig4

    else:
        print(f'hover data: {hov_data}')
        hov_year = hov_data['points'][0]['label']
        dff = df1[df1["Country Name"] == hov_year]
        dff['Year'] = dff['Year'].astype(str)
        fig4 = px.line(dff, x='Year', y="Score", color="Indicator",
                       title=f'Business Performance Indicators for:'
                             f'{hov_year} <br><sup>Select a country on the left to display performance</sup>')
        return fig4


if __name__ == '__main__':
    app.run_server(debug=True)
