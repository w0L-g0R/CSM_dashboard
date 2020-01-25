import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

from assets.styles import graph_box_title_style


def standard_box(icon: html, title: str, height: int, graph: callable):

    box = html.Div(
        style={
            "background": "rgba(0,0,0,0)",
            "margin": 5,
            "margin-right": 0,
            "margin-bottom": 0,
            "height": height,
            "border": "1px rgba(173, 216, 230, 0.3) solid",
        },
        children=[
            # TITLE ROW
            dbc.Row(
                justify="center",
                style={
                    # "width": "100%",
                    # "display": "block",
                    # # "align-items": "center",
                    # "justify-content": "center",
                    # "padding": 10
                    "text-align": "center",
                    "background": "rgba(255,0,0,0)",
                },
                # style={"background": "rgba(173, 216, 230, 0.3)"},
                no_gutters=True,
                children=[
                    # ICON
                    dbc.Col(
                        width=12,
                        children=[
                            html.Div(
                                style=graph_box_title_style, children=[icon, title]
                            )
                        ],
                    )
                ],
            ),
            # GRAPH ROW
            dbc.Row(
                no_gutters=True,
                children=[
                    # GRAPH
                    dbc.Col(
                        width=12,
                        children=[
                            html.Div(
                                style={"width": "100%", "display": "block"},
                                children=graph,
                            )
                        ],
                    )
                ],
            ),
        ],
    )

    return box


def control_box(
    icon: html,
    title: str,
    height: int,
    graph: callable,
    control: dcc,
    control_style: dict,
):

    box = html.Div(
        style={
            "background": "rgba(0,0,0,0)",
            "margin": 5,
            "margin-right": 0,
            "margin-bottom": 0,
            "height": height,
            "border": "1px rgba(173, 216, 230, 0.3) solid",
        },
        children=[
            # TITLE ROW
            dbc.Row(
                justify="center",
                style={
                    # "width": "100%",
                    # "display": "block",
                    # # "align-items": "center",
                    # "justify-content": "center",
                    # "padding": 10
                    "margin": 0,
                    "text-align": "center",
                    "background": "rgba(255,0,0,0)",
                },
                # style={"background": "rgba(173, 216, 230, 0.3)"},
                no_gutters=True,
                children=[
                    # ICON
                    dbc.Col(
                        width=12,
                        children=[
                            html.Div(
                                style=graph_box_title_style, children=[icon, title]
                            )
                        ],
                    )
                ],
            ),
            # GRAPH ROW
            dbc.Row(
                justify="center",
                no_gutters=True,
                style={
                    # "width": "100%",
                    # "display": "block",
                    # # "align-items": "center",
                    # "justify-content": "center",
                    "margin": 0,
                    "padding-bottom": 0,
                    # "text-align":"center",
                    # "background": "rgba(255,0,0,0)",
                },
                children=[
                    # GRAPH
                    dbc.Col(
                        width=12,
                        children=html.Div(
                            style={"width": "100%", "display": "block", "margin": 0},
                            children=graph,
                        ),
                    ),
                    # CONTROL
                    dbc.Col(
                        width=12,
                        children=[html.Div(style=control_style, children=control)],
                    ),
                ],
            ),
        ],
    )

    return box


def rfm_box(
    icon: html,
    title: str,
    height: int,
    histogram: callable,
    boxplot: callable,
    control: dcc,
):

    box = html.Div(
        style={
            "background": "rgba(0,0,0,0)",
            "margin": 5,
            "margin-right": 0,
            "margin-bottom": 0,
            "height": height,
            "border": "1px rgba(173, 216, 230, 0.3) solid",
        },
        children=[
            # TITLE ROW
            dbc.Row(
                justify="center",
                style={
                    # "width": "100%",
                    # "display": "block",
                    # # "align-items": "center",
                    # "justify-content": "center",
                    # "padding": 10
                    "margin": 0,
                    "text-align": "center",
                    "background": "rgba(255,0,0,0)",
                },
                # style={"background": "rgba(173, 216, 230, 0.3)"},
                no_gutters=True,
                children=[
                    # ICON
                    dbc.Col(
                        width=12,
                        children=[
                            html.Div(
                                style=graph_box_title_style, children=[icon, title]
                            )
                        ],
                    )
                ],
            ),
            # GRAPH ROW
            dbc.Row(
                justify="center",
                no_gutters=True,
                style={
                    # "width": "100%",
                    # "display": "block",
                    # # "align-items": "center",
                    # "justify-content": "center",
                    "margin": 0,
                    "padding-bottom": 0,
                    # "text-align":"center",
                    # "background": "rgba(255,0,0,0)",
                },
                children=[
                    # SLIDERS
                    dbc.Col(
                        width=12,
                        children=html.Div(
                            style={
                                "width": "90%",
                                "display": "block",
                                "margin-left": "auto",
                                "margin-right": "auto",
                                "padding": 25,
                                "padding-bottom": 0,
                                "border": "1px rgba(173, 216, 230, 0.3) solid",
                            },
                            children=control,
                        ),
                    ),
                    # HISTOGRAMS
                    dbc.Col(
                        width=12,
                        children=html.Div(
                            style={
                                "width": "100%",
                                "display": "block",
                                "padding": 25,
                                "padding-bottom": 0,
                            },
                            children=histogram,
                        ),
                    ),
                    # BOXPLOTS
                    dbc.Col(
                        width=12,
                        children=html.Div(
                            style={
                                "width": "100%",
                                "display": "block",
                                "padding": 25,
                                "padding-bottom": 0,
                            },
                            children=boxplot,
                        ),
                    ),
                ],
            ),
        ],
    )

    return box
