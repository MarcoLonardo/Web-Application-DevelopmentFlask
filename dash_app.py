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
df = df_country.groupby(['Year'
                        ])[['Getting Credit - Score','Resolving insolvency - Score',
                         'Starting a business - Score','Trading across borders - Score','Overall Score']].mean()
df.reset_index(inplace=True)
print(df[:5])

# Reading the cleaned and prepared dataset from the Data directory
file_path2 = Path(__file__).parent.joinpath('Data','prepared_dataset1.csv')
df_performance = pd.read_csv(file_path2)


# Reading the cleaned and prepared dataset from the Data directory
df_overall = df_performance.copy()
df_overall = df_overall.drop('Indicator', 1)
df_overall = df_overall.drop('Score',1)
df_overall = df_overall.drop_duplicates('Country Name')
df_overall.to_csv('prepvs_dataset.csv', index=False)

# Reading the cleaned and prepared dataset from the Data directory
file_path3 = Path(__file__).parent.joinpath('Data','cleaned_dataset_q3.csv')
df1 = pd.read_csv(file_path3)

# Data Preparation for Icicle
df_icicle = df1.copy()
df_icicle=df_icicle.groupby('Country Name').mean().reset_index()
# Dropping the column year because the Overall Score refers to the 5-Year Avg Performance
df_icicle = df_icicle.drop('Year',1)
df_icicle['Currency Unit']='Europe'
df_icicle.to_csv('prep_dataset.csv', index=False)


fig3 = px.icicle(df_icicle, path = [('Currency Unit'),'Country Name'],
                    values="Score",
                    color = "Score",
                    color_continuous_scale='RdBu',
                    custom_data=['Country Name'])



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
    html.P('Which countries in Europe have, on average, performed worse in 2020 and in previous years?'),
        # This is for the London area selector and the statistics panel.
        dbc.Col(width=3, children=[
            dcc.Dropdown(id="select_year",
                         options=[
                             {"label":"2016","value":2016},
                             {"label":"2017","value":2017},
                             {"label":"2018","value":2018},
                             {"label":"2019","value":2019},
                             {"label":"2020","value":2020}],
                             multi=False,
                             value=2020,
                         style={'width':'100%'}),
            # Div that will later contain a bootstrap card format showing the stats.
            html.Br(),
            html.Div(id="stats-card")

        ]),
        # Add the second column here. This is for the figure.
        dbc.Col(width=9,  children=[
            dcc.Graph(
                id='overall_score_chart',
                figure={})
]),
dbc.Row(dbc.Col(html.P(""))),
     dbc.Row([
         html.P('What problems are each of the countries facing?'),
            dcc.Dropdown(id="select_country",
                         options=[
                             {"label":"Austria","value":"Austria"},
                             {"label":"Belgium","value":"Belgium"},
                             {"label":"Cyprus","value":"Cyprus"},
                             {"label":"Estonia","value":"Estonia"},
                             {"label":"Finland","value":"Finland"},
                             {"label":"France","value":"France"},
                             {"label":"Germany","value":"Germany"},
                             {"label":"Greece","value":"Greece"},
                             {"label":"Ireland","value":"Ireland"},
                             {"label":"Italy","value":"Italy"},
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
                            value=["Austria","Belgium","Cyprus","Estonia","Finland","France","Germany",
                                   "Greece","Ireland","Ireland","Italy","Kosovo","Latvia","Lithuania",
                                   "Luxembourg","Malta","Montenegro","Netherlands","Portugal",
                                   "Slovak Republic","Slovenia","Slovenia","Spain"],
                             multi=True,
                             searchable=True,
                            clearable=False,
                            placeholder="select one or multiple countries",
                             style={'width':'100%'}),
            # Div that will later contain a bootstrap card format showing the stats.
            html.Br(),
            html.Div(id="country_selection_panel", children=[]),
            dcc.Graph(
                id='indicator_chart',
                figure={}),


dbc.Row(dbc.Col(html.P(""))),
    dbc.Row([
        html.P('How has overall performance changed by years? And how have specific indicators changed by country'),
        # This is for the London area selector and the statistics panel.
        dbc.Col(width=3, children=[
dcc.Graph(id='my-graph', figure=fig3, clickData=None, hoverData=None,
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
        # Add the second column here. This is for the figure.
                dbc.Col(width=9, children=[
                dcc.Graph(id='pie-graph',
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

def update_graph (option_selected):
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



# Adressing Question 2

@app.callback(
            [Output(component_id='country_selection_panel', component_property='children'),
             Output(component_id='indicator_chart', component_property='figure')],
    [Input(component_id='select_country', component_property='value')]
        )

def update_countries (country_selected):
    df_performance1 = df_performance[(df_performance["Country Name"].isin(country_selected))]

    container = "Selected: {}".format(country_selected)

    fig2 = px.scatter(df_performance1, x="Score", y="Overall Score", animation_frame="Year", animation_group="Country Name",
                 size="Score", color="Indicator", hover_name="Country Name", facet_col="Indicator",
            size_max=12, range_x=[0,105], range_y=[0,105])

    fig2.update_layout(height=650, width=1400)


    return container,fig2



# Addressing Question 3
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
)

def update_side_graph(hov_data):
    if hov_data is None:
        dff = df1[df1["Country Name"] == "empty"]
        fig4 = px.line(dff, x='Year', y="Score", color="Indicator",
                      title='Business Performance <br><sup>Select a country on the left to display performance</sup>')
        return fig4

    else:
        print(f'hover data: {hov_data}')
       # print(hov_data['points'][0]['customdata'][0])
        hov_year = hov_data['points'][0]['label']
        dff = df1[df1["Country Name"] == hov_year]
        fig4 = px.line(dff, x='Year', y="Score", color="Indicator",
                       title=f'Business Performance Indicators for:'
                             f'{hov_year} <br><sup>Select a country on the left to display performance</sup>')
        return fig4


if __name__ == '__main__':
    app.run_server(debug=True)
