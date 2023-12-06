import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

# 正多角形を描画する関数
def draw_polygon(n_sides, ratio1, ratio2):
    # n_sides: 正多角形の辺の数
    # 中心座標
    x_center, y_center = 0, 0
    # 半径
    radius = 1
    # 角度
    angles = [i * 2 * np.pi / n_sides for i in range(n_sides)]
    # 頂点の座標
    x = [x_center + radius * np.cos(angle) * ratio1 for angle in angles]
    y = [y_center + radius * np.sin(angle) * ratio1 for angle in angles]

    if(ratio2 == 0) :
      # 描画
      fig = px.line(x=x + [x[0]], y=y + [y[0]])
    else:
      x2 = [x_center + radius * np.cos(angle) * ratio2 for angle in angles]
      y2 = [y_center + radius * np.sin(angle) * ratio2 for angle in angles]
      # 描画
      fig = px.line(x=x + [x[0]] + x2 + [x2[0]], y=y + [y[0]] + y2 + [y2[0]])
    
    fig.update_traces(mode='lines+markers')

    return fig

# Webアプリケーションを作成する
app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.Label('円と正方形の周りの長さを比較する', style={'font-size': '32px'}),
        html.Br(),
        html.Label('　ここに表示した正方形と円の周囲の長さは等しいですか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　ちょっと迷ってしまいますね？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　同じ形であれば、隣に並べたり上に重ねたりすることで比較できますが、', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　形が異なる図形はどうやって比較したら良いのでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　では正方形と円どちらかの周りの長さや大きさを比べたいときには、', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　小学5年生で習う「円周率≒3.14」を使うと便利です。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　半径が1の円の周りの長さ（円周）は「円周率の2倍≒6.28」ですね。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　「円周率の2倍≒6.28」を四等分した長さ「円周率の2倍÷4≒1.57」が正方形の一辺の長さですね。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　では、他の正多角形の一辺の長さも求めてみましょう！', style={'font-size': '16px'}),
        html.Br(),
        dcc.Graph(
            id='polygon-graph1',
            figure={
                'data': [],
                'layout': {
                    'width': 1000,  # グラフの幅
                    'height': 1000,  # グラフの高さ
                    'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},  # マージン
                    'paper_bgcolor': '#f8f9fa',  # 背景色
                    'plot_bgcolor': '#f8f9fa',  # プロット領域の背景色
                }
            }
        ),
    ]), 
    html.Label('辺の数'),
    dcc.Input(id='n-sides-input1', type='number', value=4, min=3, max=100),
    
    html.Div([
        html.Label('円と正方形の周りの長さを比較する', style={'font-size': '32px'}),
        html.Br(),
        html.Label('　ここに正方形と円があった場合、周りの長さは同じになるでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　それともどちらが大きい（長い）でしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　同じ形の場合は、並べたり重ねたりすることで比較できますが、', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　形が異なる場合はどうやって比較したら良いのでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　そんな正方形と円どちらかの周りの長さや大きさを比べたいときには、', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　小学5年生で習う「円周率は3.14」を使うと便利です。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　1辺の長さが1の正方形の周りの長さは4ですね。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　それでは、周りの長さが同じになるような円はどのように書けばよいでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        dcc.Graph(
            id='polygon-graph2',
            figure={
                'data': [],
                'layout': {
                    'width': 1000,  # グラフの幅
                    'height': 1000,  # グラフの高さ
                    'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},  # マージン
                    'paper_bgcolor': '#f8f9fa',  # 背景色
                    'plot_bgcolor': '#f8f9fa',  # プロット領域の背景色
                }
            }
        ),
    ]), 
    html.Label('辺の数'),
    dcc.Input(id='n-sides-input2', type='number', value=4, min=3, max=100),

    html.Div([
        html.Label('円と正方形の周りの長さを比較する', style={'font-size': '32px'}),
        html.Br(),
        html.Label('　ここに正方形と円があった場合、周りの長さは同じになるでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　それともどちらが大きい（長い）でしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　同じ形の場合は、並べたり重ねたりすることで比較できますが、', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　形が異なる場合はどうやって比較したら良いのでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　そんな正方形と円どちらかの周りの長さや大きさを比べたいときには、', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　小学5年生で習う「円周率は3.14」を使うと便利です。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　1辺の長さが1の正方形の周りの長さは4ですね。', style={'font-size': '16px'}),
        html.Br(),
        html.Label('　それでは、周りの長さが同じになるような円はどのように書けばよいでしょうか？', style={'font-size': '16px'}),
        html.Br(),
        dcc.Graph(
            id='polygon-graph3',
            figure={
                'data': [],
                'layout': {
                    'width': 1000,  # グラフの幅
                    'height': 1000,  # グラフの高さ
                    'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},  # マージン
                    'paper_bgcolor': '#f8f9fa',  # 背景色
                    'plot_bgcolor': '#f8f9fa',  # プロット領域の背景色
                }
            }
        ),
    ]), 
    html.Label('辺の数'),
    dcc.Input(id='n-sides-input3', type='number', value=4, min=3, max=100),
])

# コールバック関数を定義する
@app.callback(
    [dash.dependencies.Output('polygon-graph1', 'figure'),
     dash.dependencies.Output('polygon-graph2', 'figure'),
     dash.dependencies.Output('polygon-graph3', 'figure')],
    [dash.dependencies.Input('n-sides-input1', 'value'),
     dash.dependencies.Input('n-sides-input2', 'value'),
     dash.dependencies.Input('n-sides-input3', 'value')],
    )
def update_polygon(n_sides1, n_sides2, n_sides3):
    fig1 = draw_polygon(n_sides1, np.pi / n_sides1 / np.cos(np.pi * (1 / 2 - 1 / n_sides1)), 0)
    fig1.add_shape(
        type='circle',
        xref='x', yref='y',
        x0=-1, y0=-1, x1=1, y1=1,
        line=dict(color='Green', width=4),
    )
    fig2 = draw_polygon(n_sides2, np.sqrt(np.pi / n_sides2 / np.sin(np.pi / n_sides2) / np.cos(np.pi / n_sides2)), 0)
    fig2.add_shape(
        type='circle',
        xref='x', yref='y',
        x0=-1, y0=-1, x1=1, y1=1,
        line=dict(color='Green', width=4),
    )
    fig3 = draw_polygon(n_sides3, 1, 1 / np.cos(np.pi / n_sides3))
    fig3.add_shape(
        type='circle',
        xref='x', yref='y',
        x0=-1, y0=-1, x1=1, y1=1,
        line=dict(color='Green', width=4),
    )

    return fig1, fig2, fig3

if __name__ == '__main__':
    app.run_server(debug=True)