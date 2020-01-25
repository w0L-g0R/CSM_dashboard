import dash
import dash_bootstrap_components as dbc

import pandas as pd
import os

import pickle

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[
        {
            "href": "https://use.fontawesome.com/releases/v5.8.1/css/all.css",
            "rel": "stylesheet",
            "integrity": "sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf",
            "crossorigin": "anonymous",
        },
        dbc.themes.BOOTSTRAP,
    ],
)
app.config['suppress_callback_exceptions']=True
app.title = "CSM-DASHBOARD"
server = app.server
