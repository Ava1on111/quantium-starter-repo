import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 加载你的数据
df = pd.read_csv('output.csv')

# 初始化Dash应用
app = dash.Dash(__name__)

# 应用布局
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
        value='all',  # 默认值
        className='radioitems'
    ),

    dcc.Graph(
        id='sales-chart',
        className='chart'
    )
])

# 回调函数更新图表
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_chart(selected_region):
    filtered_df = df if selected_region == 'all' else df[df['region'] == selected_region]

    # 创建线图
    fig = px.line(filtered_df, x='date', y='sales', title='Sales Over Time')

    # 设置图表的X和Y轴标签
    fig.update_layout(xaxis_title='Date', yaxis_title='Sales')

    return fig

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)