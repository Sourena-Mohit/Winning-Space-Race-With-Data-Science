import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# -------------------------
# Load data
# -------------------------
# If you already downloaded spacex_launch_dash.csv locally, use:
# spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Otherwise load directly from the web:
spacex_df = pd.read_csv(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
)

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# -------------------------
# Create Dash app
# -------------------------
app = dash.Dash(__name__)

# TASK 1: Add a Launch Site Drop-down Input Component
launch_sites = sorted(spacex_df['Launch Site'].unique())
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
               [{'label': site, 'value': site} for site in launch_sites]

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36',
                   'font-size': 40}),

    # Dropdown
    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),

    # Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: Add a Range Slider to Select Payload
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),
    html.Br(),

    # Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# ------------------------------------------------
# TASK 2: Callback for success-pie-chart
# ------------------------------------------------
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # total successful launches by site (class==1)
        success_by_site = spacex_df.groupby('Launch Site')['class'].sum().reset_index()

        fig = px.pie(
            success_by_site,
            values='class',
            names='Launch Site',
            title='Total Success Launches By Site'
        )
        return fig
    else:
        # success vs failure for one selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]

        outcome_counts = filtered_df['class'].value_counts().reset_index()
        outcome_counts.columns = ['class', 'count']
        outcome_counts['class'] = outcome_counts['class'].map({1: 'Success', 0: 'Failure'})

        fig = px.pie(
            outcome_counts,
            values='count',
            names='class',
            title=f'Total Success Launches for site {entered_site}'
        )
        return fig


# ------------------------------------------------
# TASK 4: Callback for success-payload-scatter-chart
# ------------------------------------------------
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range

    # filter by payload range first
    df_filtered = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if entered_site != 'ALL':
        df_filtered = df_filtered[df_filtered['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for site {entered_site}'
    else:
        title = 'Correlation between Payload and Success for all Sites'

    fig = px.scatter(
        df_filtered,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=title
    )
    return fig


# -------------------------
# Run
# -------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=False)
