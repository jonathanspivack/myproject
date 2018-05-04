# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              [Input('input-2-state', 'value')],
              [State('input-1-state', 'value')])
def update_output(input1, input2):
    return u'''
        The Button has been pressed  timesz,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)