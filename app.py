# app.py

import dash
from dash import dcc, html

# Create a Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout of the app
app.layout = html.Div([
    html.H1("Hello Dash!"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'Example'},
            ],
            'layout': {
                'title': 'Simple Graph Example'
            }
        }
    )
])

# Run the server if the script is run directly
if __name__ == '__main__':
    app.run_server(debug=True)
