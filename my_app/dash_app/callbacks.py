from pathlib import Path
from dash import dcc, Input, Output
from dash import dash, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly_express as px

# Reading and preparing the dataset for the choropleth (visualization 1).
file_path = Path(__file__).parent.joinpath('Data', 'prepared_dataset.csv')
df_country = pd.read_csv(file_path)
df = df_country.groupby(['Year'])[['Getting Credit - Score', 'Resolving insolvency - Score',
                                   'Starting a business - Score', 'Trading across borders - Score',
                                   'Overall Score']].mean()
df.reset_index(inplace=True)
print(df[:5])

# Reading the second version of the prepared dataset with different data structure for the scatter map (visualization 2)
file_path2 = Path(__file__).parent.joinpath('Data', 'prepared_dataset_v2.csv')
df_performance = pd.read_csv(file_path2)

# Removing irrelevant columns and duplicates from a new dataframe variable
df_overall = df_performance.copy()
df_overall = df_overall.drop('Indicator', 1)
df_overall = df_overall.drop('Score', 1)
df_overall = df_overall.drop_duplicates('Country Name')

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

def register_callbacks(dash_app):
    @dash_app.callback(
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
                # Adapted from code written by user parasmadan15  on GeeksforGeeks at
                # https://www.geeksforgeeks.org/get-a-list-of-a-particular-column-values-of-a-pandas-dataframe/
                # Accessed 07/02/2022
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
            hover_name="Country Name",
            title="Overall Score across Europe"
        )

        # Updating the layout and hiding countries not politically involved in the EU
        fig.update_layout(height=650, width=900)
        fig.update_geos(fitbounds="locations", visible=True)

        return card, fig

    @dash_app.callback(
        [Output(component_id='country_selection_panel', component_property='children'),
         Output(component_id='scatter_indicator_chart', component_property='figure')],
        [Input(component_id='select_country', component_property='value')]
    )
    # Adding interactivity to the scatter map chart
    def update_countries(country_selected):
        # Filtering the dataset using the values selected from the multi-select dropdown.
        # Adapted from code written by user qdumont community.plotly at
        # https://community.plotly.com/t/callbacks-with-a-drop-down-with-multi-select/11235/5 Accessed 10/02/2022
        df_performance1 = df_performance[(df_performance["Country Name"].isin(country_selected))]

        container = "Selected: {}".format(country_selected)

        fig2 = px.scatter(df_performance1, x="Score", y="Overall Score", animation_frame="Year",
                          animation_group="Country Name",
                          size="Score", color="Indicator", hover_name="Country Name", facet_col="Indicator",
                          size_max=12, range_x=[0, 105], range_y=[0, 105])

        fig2.update_layout(height=650, width=1400)

        return container, fig2

    @dash_app.callback(
        Output(component_id='line_graph', component_property='figure'),
        Input(component_id='icicle', component_property='hoverData'),
    )
    # Interactivity to the the line chart: updating the line chart countries on hovering over the countries in the
    # icicle
    def update_line_graph(hov_data):
        # Filter the dataframe only for the values that have been hovered. Adapted from code written by
        # Coding-with-Adam on Github at https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Dash
        # %20Components/Graph/dash-graph.py Accessed 14/02/2022
        if hov_data is None:
            dff = df1[df1["Country Name"] == "empty"]
            fig4 = px.line(dff, x='Year', y="Score", color="Indicator",
                           title='Business Performance <br><sup>Select a country on the left to display '
                                 'performance</sup>')
            return fig4

        else:
            print(f'hover data: {hov_data}')
            hov_year = hov_data['points'][0]['label']
            dff = df1[df1["Country Name"] == hov_year]
            # Prevent conversion to float. Adapted from code written by AmourK on stackoverflow at
            # https://stackoverflow.com/questions/48715330/pandas-plotting-x-axis-gets-transformed-to-floats
            # Accessed 14/02/2022
            dff['Year'] = dff['Year'].astype(str)
            fig4 = px.line(dff, x='Year', y="Score", color="Indicator",
                           title=f'Business Performance Indicators for:'
                                 f'{hov_year} <br><sup>Select a country on the left to display performance</sup>')
            return fig4
