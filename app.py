# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


import dash_vtk
from dash_vtk.utils import to_mesh_state

try:
    # VTK 9+
    from vtkmodules.vtkImagingCore import vtkRTAnalyticSource
except ImportError:
    # VTK =< 8
    from vtk.vtkImagingCore import vtkRTAnalyticSource

def read_stl(stl_file):
    txt_content = None
    with open(stl_file, 'r') as file:
      txt_content = file.read()

    content = dash_vtk.View([
        dash_vtk.GeometryRepresentation([
            dash_vtk.Reader(
                vtkClass="vtkSTLReader",
                parseAsText=txt_content,
            ),
        ]),
    ])
    return content

stl_file_35 = "./assets/datasets/design_35.stl"
des_35 = read_stl(stl_file_35)

stl_file_445 = "./assets/datasets/design_445.stl"
des_445 = read_stl(stl_file_445)

stl_file_1096 = "./assets/datasets/design_1096.stl"
des_1096 = read_stl(stl_file_1096)

# Themes: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = Dash(__name__, title='UAV Designverse', external_stylesheets=[dbc.themes.DARKLY])
# DARKLY colors: https://github.com/thomaspark/bootswatch/blob/c143eda36a068054ebad9b4c80314c40f13c9c10/docs/5/darkly/_variables.scss
server = app.server

colors = {
    'background': '#222',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.Div(
        className="app-header",
        children=[
            html.Div('AircraftVerse', className="app-header--title")
        ],
        style={
            'color': colors['text']
              }
    ),

    html.A([
    html.Img(src='./assets/nusci.jpg', style={
        'display': 'inline-block',
        'position': 'absolute',
        'height': '60px',
        'top':'5px',
        'left':'10px'
        # "height": "3%"
    },),], href='https://nusci.csl.sri.com/'),

    html.A([
    html.Img(src='./assets/sri-logo-short-color.png', style={
        'display': 'inline-block',
        'position': 'absolute',
        'height': '50px',
        'top':'15px',
        'right':'10px'
        # "height": "3%"
    },),], href = 'https://www.sri.com/'),

    html.Center([

    html.Div(children='We present AircraftVerse, a publicly available unmanned air vehicle (UAV) design dataset. UAV design encompasses different physics domains and, hence, multiple modalities of representation.  The evaluation of these designs requires the use of scientific analytical and simulation models ranging from computer-aided design tools for structural and manufacturing analysis, computational fluid dynamics tools for drag and lift computation, battery models for energy estimation, and simulation models for flight control and dynamics.',
    style={
        'textAlign': 'center',
        'color': colors['text'],
        'width': '80%',
        'padding': '32px 32px'
    }),



    # First graph

    html.Div(
    # style={"width": "100%", "height": "400px"},
    children=[des_35],
    style={
        'display': 'inline-block',
        'vertical-align': 'top',
        'width': '33%',
        "height": "200px",
        'padding': '8px 0px'
    },
    ),

    # Second graph
    html.Div(
    # style={"width": "100%", "height": "400px"},
    children=[des_445],
    style={
        'display': 'inline-block',
        'vertical-align': 'top',
        'width': '33%',
        "height": "200px",
        'padding': '8px 0px'
    },
    ),

    # Third graph
    html.Div(
    # style={"width": "100%", "height": "400px"},
    children=[des_1096],
    style={
        'display': 'inline-block',
        'vertical-align': 'top',
        'width': '33%',
        "height": "200px",
        'padding': '8px 0px'
    },
    ),

    html.Div(
    # style={"width": "100%", "height": "400px"},
    children=['Use the mouse to manipulate the UAV designs in the figures above.'],
    style={
        # 'display': 'inline-block',
        'vertical-align': 'top',
        'width': '80%',
        # "height": "200px",
        'padding': '8px 0px'
    },
    ),

    html.A([html.Button('Dataset', id='btn-nclicks-1', n_clicks=0, className = "button button2"),], href = 'https://www.sri.com/'),
    html.A([html.Button('Paper', id='btn-nclicks-2', n_clicks=0, className = "button button2"),], href = 'https://www.sri.com/'),
    html.A([html.Button('Explore Designs', id='btn-nclicks-3', n_clicks=0, className = "button button2"),], href = 'https://www.sri.com/'),

    dcc.Markdown('''### Acknowledgements

This project was supported by DARPA under the Symbiotic
Design for Cyber-Physical Systems (SDCPS) with contract
FA8750-20-C-0002.
The views, opinions and/or findings expressed
are those of the author and should not be interpreted as
representing the official views or policies of the Department
of Defense or the U.S. Government.
This dataset was developed as a collaboration between 
researchers at SRI International, 
SwRI, Vanderbilt and CMU.''', style = {'textAlign': 'center',
'color': colors['text'], 'width': '80%'} )

    ]),

    ])




if __name__ == '__main__':
    app.run_server(debug=True)
