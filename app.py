import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('output.csv')
# Remove the $
df['sales'] = df['sales'].str.replace('$', '').astype(float)

# Create dash
app = dash.Dash(__name__)

# Create a line chart
fig = px.line(df, x='date', y='sales', title='Pink Morsel Sales Over Time')
fig.update_layout(xaxis_title='Date', yaxis_title='Sales')

# Define app layout
app.layout = html.Div(children=[
    html.H1(children='Soul Foods Sales Visualiser'),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)