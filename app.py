import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('output.csv')

app = dash.Dash(__name__)

# Layout
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualiser'),

    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all', 
        className='radioitems'
    ),

    dcc.Graph(
        id='sales-chart',
        className='chart'
    )
])

# Callback function to update chart
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    filtered_df = df if selected_region == 'all' else df[df['region'] == selected_region]

    # Create the line chart
    fig = px.line(filtered_df, x='date', y='sales', title='Sales Over Time')

    # Set the chart's X and Y axis labels
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales')

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)