import dash
import pickle
import base64
import dash_table_experiments as dt
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sklearn.externals import joblib


## Read in data 
performance_coffcients_table = pd.read_pickle("riw0xt_testing.pkl")
table = pd.DataFrame.from_dict(performance_coffcients_table)
cofficients = table[['Coefficients', 'Standard Errors', 'p-values', 't-values']]
performance = table[['VIF', 'MAE', 'MSE']]
performance = performance.dropna()

## The app
app = dash.Dash(__name__)

## Load images
preds_image_filename = 'pred_test.png'
encoded_image = base64.b64encode(open(preds_image_filename, 'rb').read())

resdiuals_image_filename = 'res_test.png'
encoded_image2 = base64.b64encode(open(resdiuals_image_filename, 'rb').read())

qq_image_filename = 'qq_test.png'
encoded_image3 = base64.b64encode(open(qq_image_filename, 'rb').read())

corr_image_filename = 'corr.png'
encoded_image4 = base64.b64encode(open(corr_image_filename, 'rb').read())

scatter_image_filename = 'scatter.png'
encoded_image5 = base64.b64encode(open(scatter_image_filename, 'rb').read())

distribution_image_filename = 'tv_spend.png'
encoded_image6 = base64.b64encode(open(distribution_image_filename, 'rb').read())

kde_image_filename = 'distribution.png'
encoded_image7 = base64.b64encode(open(kde_image_filename, 'rb').read())

joint_image_filename = 'joint_plot.png'
encoded_image8 = base64.b64encode(open(joint_image_filename, 'rb').read())

## Create the layout
app.layout = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='EDA', value='tab-1'),
        dcc.Tab(label='Model #1', value='tab-2'),
        dcc.Tab(label='Model #2', value='tab-3'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
                html.Img(src='data:image/png;base64,{}'.format(encoded_image4.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image5.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image6.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image8.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image7.decode())),
            ])

    elif tab == 'tab-2':
        return html.Div([
                html.H4('Coefficients DataTable'),
                dt.DataTable(
                rows=cofficients.to_dict('records'),
                # optional - sets the order of columns
                columns=sorted(cofficients.columns),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                id='datatable-coefficients'
            ),

                html.H4('Model Performance DataTable'),
                dt.DataTable(
                rows=performance.to_dict('records'),
                # optional - sets the order of columns
                columns=sorted(performance.columns),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                id='datatable-performance'
            ),

                html.Div([

                html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode())),

                ])

        ])

    elif tab == 'tab-3':
        return html.Div([
                html.H4('Coefficients DataTable'),
                dt.DataTable(
                rows=cofficients.to_dict('records'),
                # optional - sets the order of columns
                columns=sorted(cofficients.columns),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                id='datatable-coefficients'
            ),

                html.H4('Model Performance DataTable'),
                dt.DataTable(
                rows=performance.to_dict('records'),
                # optional - sets the order of columns
                columns=sorted(performance.columns),
                row_selectable=True,
                filterable=True,
                sortable=True,
                selected_row_indices=[],
                id='datatable-performance'
            ),

                html.Div([

                html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode())),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image3.decode())),

                ])

        ])

if __name__ == '__main__':
    app.run_server(debug=True)
