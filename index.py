import os
import pandas as pd
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server
from assets.styles import container_style, body_style
from components.navbar import navbar

from layouts import (
    serve_key_facts_layout, 
    serve_metrics_layout, 
    serve_segments_layout,
    serve_premium_content_layout
)

from callbacks import update_map_figure, update_rfm_figures


"""####################################################################"""
"""                              MAIN LAYOUT                           """
"""####################################################################"""

app.layout = dbc.Container(
    fluid=True,
    style=container_style,
    children=[
        dbc.Row(
            no_gutters=True,
            children=[
                navbar,
                dbc.Col(
                    xs=12,
                    sm=12,
                    md=12,
                    lg=12,
                    xl=10,
                    style=body_style,
                    width={"offset": 0},
                    children=[html.Div(id="body-content")],
                ),
            ],
        )
    ],
)

"""####################################################################"""
"""                              ROUTING                               """
"""####################################################################"""


@app.callback(Output("body-content", "children"), [Input("nav-tabs", "value")])
def render_content(tab):

    # KEY FACTS
    if tab == "tab-1":
        return serve_key_facts_layout()

    # METRICS
    elif tab == "tab-2":
        return serve_metrics_layout()

    # CS
    elif tab == "tab-3":
        return serve_segments_layout()

    # CLV
    elif tab == "tab-4":
        return serve_premium_content_layout()

    # CHURN
    elif tab == "tab-5":
        return serve_premium_content_layout()

    # NPD
    elif tab == "tab-6":
        return serve_premium_content_layout()

    # SALES
    elif tab == "tab-7":
        return serve_premium_content_layout()

    # MR
    elif tab == "tab-8":
        return serve_premium_content_layout()

    # UPLIFT
    elif tab == "tab-9":
        return serve_premium_content_layout()

    # A/B
    elif tab == "tab-10":
        return serve_premium_content_layout()


"""####################################################################"""
"""                               RUN                                  """
"""####################################################################"""

if __name__ == "__main__":
    app.run_server(debug=True)
