from pathlib import Path
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly_express as px

# Reading the third version of the prepared dataset with different data structure for visualization 3
file_path3 = Path(__file__).parent.joinpath('Data', 'prepared_dataset_v3.csv')
df1 = pd.read_csv(file_path3)

# Data Preparation for Icicle
df_icicle = df1.copy()
# Calculating the average 5-year performance. Based on code written by user Alex on stackoverflow at
# https://stackoverflow.com/questions/48366506/calculate-new-column-as-the-mean-of-other-columns-pandas/48366525
# Accessed 11/02/2022
df_icicle = df_icicle.groupby('Country Name').mean().reset_index()
# Dropping the column year because the Overall Score refers to the 5-Year Avg Performance
df_icicle = df_icicle.drop('Year', 1)
# Creating a new column for the Icicle Root Node. Based on code written by user EdChum on stackoverflow at
# https://stackoverflow.com/questions/29517072/add-column-to-dataframe-with-constant-value Accessed 05/02/2022
df_icicle['Currency Unit'] = 'Europe'

fig3 = px.icicle(df_icicle, path=['Currency Unit', 'Country Name'], values="Score", color="Score",
                 color_continuous_scale='BrBG', range_color=[65, 85], custom_data=['Country Name'])

fig3.update_layout(
    uniformtext=dict(minsize=50), margin=dict(t=50, l=25, r=25, b=25))

layout = dbc.Container(fluid=True, children=[
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
        html.P('Which countries have the lowest/highest Overall Score for every year and how does this '
               'compare with the European Average?'),
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
            html.P('Which challenges have the European countries been facing from 2016 to 2020?'),
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
                    'Across the four indicators, has the performance of each country been increasing or '
                    'decreasing from 2016 to 2020?'),
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
