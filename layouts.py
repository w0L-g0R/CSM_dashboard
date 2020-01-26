import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from app import app

from assets.styles import (
    header_box_style,
    key_facts_logo_style,
    key_facts_title_style,
    key_facts_subtitle_style,
    key_facts_boxes_style,
    key_facts_period_style,
    key_facts_period_title_style
)

from plot import (
    monthly,
    retention_monthly,
    retention_cohort,
    segments_3D,
    segments_treemap,
    indicator_plot,
)

from components.icons import *
from components.boxes import standard_box, rfm_box, control_box


"""####################################################################"""
"""                             KEY FACTS                              """
"""####################################################################"""


def serve_key_facts_layout():

    content = (
        html.Div(
            children=[
                # LOGO ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            xs=12,
                            sm=12,
                            md=12,
                            lg=12,
                            xl=12,
                            children=html.Img(
                                src=app.get_asset_url("furniture_logo.png"),
                                style=key_facts_logo_style,
                            ),
                        )
                    ],
                ),
                # MAIN TITLE ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            xs=12,
                            sm=12,
                            md=12,
                            lg=12,
                            xl=12,
                            children=html.Div(
                                children="Funny Furniture", style=key_facts_title_style
                            ),
                        )
                    ],
                ),
                # SUBTITLE ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            xs=12,
                            sm=12,
                            md=12,
                            lg=12,
                            xl=12,
                            children=html.Div(
                                children="Online retailer for household commodities and interior decoration since 1995",
                                style=key_facts_subtitle_style,
                            ),
                        )
                    ],
                ),

                # SUBTITLE ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            width=12,
                            children=html.Div(
                                children="KEY FACTS",
                                style=key_facts_period_title_style,
                            ),
                        )
                    ],
                ),
                # FACTS ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    style={"margin-right": 140},
                    children=[
                        dbc.Col(
                            xs=4,
                            sm=4,
                            md=4,
                            lg=1,
                            xl=1,
                            children=html.Div(
                                children=indicator_plot(name="customers"),
                                style=key_facts_boxes_style,
                            ),
                        ),
                        dbc.Col(
                            xs=4,
                            sm=4,
                            md=4,
                            lg=1,
                            xl=1,
                            children=html.Div(
                                children=indicator_plot(name="countries"),
                                style=key_facts_boxes_style,
                            ),
                        ),
                        dbc.Col(
                            xs=4,
                            sm=4,
                            md=4,
                            lg=1,
                            xl=1,
                            children=html.Div(
                                children=indicator_plot(name="quantities"),
                                style=key_facts_boxes_style,
                            ),
                        ),
                        dbc.Col(
                            xs=4,
                            sm=4,
                            md=4,
                            lg=1,
                            xl=1,
                            children=html.Div(
                                children=indicator_plot(name="orders"),
                                style=key_facts_boxes_style,
                            ),
                        ),
                        dbc.Col(
                            xs=4,
                            sm=4,
                            md=4,
                            lg=1,
                            xl=1,
                            children=html.Div(
                                children=indicator_plot(name="products"),
                                style=key_facts_boxes_style,
                            ),
                        ),
                        dbc.Col(
                            xs=4,
                            sm=4,
                            md=4,
                            lg=1,
                            xl=1,
                            children=html.Div(
                                children=indicator_plot(name="revenues"),
                                style=key_facts_boxes_style,
                            ),
                        ),
                    ],
                ),
                # SUBTITLE ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            width=12,
                            children=html.Div(
                                children="February - November 2019",
                                style=key_facts_period_style,
                            ),
                        )
                    ],
                ),
            ]
        ),
    )

    return content


"""####################################################################"""
"""                               METRICS                              """
"""####################################################################"""


def metrics_column(icon: str, graph: callable, title: str):

    column = dbc.Col(
        xs=12,
        sm=12,
        md=4,
        lg=4,
        xl=4,
        children=standard_box(icon=icon, height=335, title=title, graph=graph),
    )
    return column


map_radio_items = dbc.RadioItems(
    style={
        "font-family": "Oswald ExtraLight, sans-serif",
        "font-size": 14,
        "color": "white",
    },
    options=[{"label": "Revenues", "value": 1}, {"label": "Customers", "value": 2}],
    value=1,
    id="map-radio-items",
    inline=True,
    inputStyle={"color": "lightblue"},
)


def serve_metrics_layout():

    content = html.Div(
        style={"margin-right": 5},
        children=[
            # HEADER ROW
            dbc.Row(
                no_gutters=True,
                children=[
                    dbc.Col(
                        width=12,
                        children=html.Div(
                            style=header_box_style, children="BUSINESS METRICS"
                        ),
                    )
                ],
            ),
            # ROW 1
            dbc.Row(
                no_gutters=True,
                children=[
                    # REVENUES
                    metrics_column(
                        icon=revenues_icon,
                        title="Monthly Revenues",
                        graph=monthly(revenues=True),
                    ),
                    # ACTIVE CUSTOMERS
                    metrics_column(
                        icon=customers_icon,
                        title="Monthly Active Customers",
                        graph=monthly(customers=True),
                    ),
                    # ORDERS
                    metrics_column(
                        icon=orders_icon,
                        title="Monthly Orders",
                        graph=monthly(orders=True),
                    ),
                ],
            ),
            # ROW 2
            dbc.Row(
                no_gutters=True,
                children=[
                    # MAP
                    dbc.Col(
                        xs=12,
                        sm=12,
                        md=4,
                        lg=4,
                        xl=4,
                        children=[
                            control_box(
                                icon=map_icon,
                                title="Per Country Data",
                                graph=dcc.Graph(id="per-country-map-graph"),
                                control=map_radio_items,
                                control_style={
                                    "width": "100%",
                                    "display": "block",
                                    "text-align": "center",
                                    "padding-left": 30,
                                },
                                height=335,
                            )
                        ],
                    ),
                    # MONTHLY RETENTION
                    metrics_column(
                        icon=retention_icon,
                        title="Monthly Retention Rates",
                        graph=retention_monthly(),
                    ),
                    # COHORT RETENTION
                    metrics_column(
                        icon=cohort_icon,
                        title="Cohort Retention Rates",
                        graph=retention_cohort(),
                    ),
                ],
            ),
        ],
    )

    return content


"""####################################################################"""
"""                        CUSTOMER SEGMENTS                           """
"""####################################################################"""


def segments_column(icon: str, graph: callable, title: str):

    column = dbc.Col(
        xs=12,
        sm=12,
        md=6,
        lg=6,
        xl=6,
        children=standard_box(icon=icon, height=335, title=title, graph=graph),
    )

    return column


histogram_slider = dcc.Slider(
    id="slider-histogram",
    min=0,
    max=2,
    step=1,
    marks={0: "Recency", 1: "Frequency", 2: "Monetary"},
    value=0,
)


def serve_segments_layout():

    content = html.Div(
        style={"margin-right": 5},
        children=[
            # HEADER ROW
            dbc.Row(
                no_gutters=True,
                children=[
                    dbc.Col(
                        width=12,
                        children=html.Div(
                            style=header_box_style, children="CUSTOMER SEGMENTS"
                        ),
                    )
                ],
            ),
            # BODY ROW
            dbc.Row(
                no_gutters=True,
                children=[
                    # LEFT COL
                    dbc.Col(
                        xs=12,
                        sm=12,
                        md=12,
                        lg=5,
                        xl=5,
                        children=[
                            # SLIDERS
                            dbc.Row(
                                style={"width": "100%"},
                                no_gutters=True,
                                children=[
                                    # SLIDER
                                    dbc.Col(
                                        xs=12,
                                        sm=12,
                                        md=12,
                                        lg=12,
                                        xl=12,
                                        children=[
                                            rfm_box(
                                                icon=rfm_distribution_icon,
                                                title="RFM Clusters",
                                                histogram=dcc.Graph(
                                                    id="RFM-histogram-graph"
                                                ),
                                                boxplot=dcc.Graph(
                                                    id="RFM-boxplots-graph"
                                                ),
                                                control=histogram_slider,
                                                height=675,
                                            )
                                        ],
                                    )
                                ],
                            )
                        ],
                    ),
                    # RIGHT COL
                    dbc.Col(
                        xs=12,
                        sm=12,
                        md=12,
                        lg=7,
                        xl=7,
                        children=[
                            # SEGMENTS
                            dbc.Row(
                                no_gutters=True,
                                children=[
                                    # SEGMENTS TREEMAP
                                    dbc.Col(
                                        xs=12,
                                        sm=12,
                                        md=12,
                                        lg=12,
                                        xl=12,
                                        children=[
                                            standard_box(
                                                icon=segments_treemap_icon,
                                                title="Customer Segments",
                                                graph=segments_treemap(),
                                                height=220,
                                            )
                                        ],
                                    )
                                ],
                            ),
                            # 3D SEGMENTS
                            dbc.Row(
                                no_gutters=True,
                                children=[
                                    dbc.Col(
                                        xs=12,
                                        sm=12,
                                        md=12,
                                        lg=12,
                                        xl=12,
                                        children=[
                                            standard_box(
                                                icon=html.Div(),
                                                title="",
                                                graph=segments_3D(),
                                                height=450,
                                            )
                                        ],
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )

    return content

"""####################################################################"""
"""                        PREMIUM CONTENT                             """
"""####################################################################"""


def serve_premium_content_layout():

    content = (
        html.Div(
            children=[

                # MAIN TITLE ROW
                dbc.Row(
                    justify="center",
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            width=12,
                            children=html.Div(
                                children="PREMIUM CONTENT", style={
                                "display":"block",
                                "text-align":"center",
                                "margin-top":"25%",
                                # "margin-bottom":"50%",
                                "font-family": "Oswald Stencil, sans-serif",
                                "font-size": 78,
                                 "color": "white",
                                }
                            ),
                        ),

                    # LOGO ROW
                    dbc.Row(
                        justify="center",
                        no_gutters=True,
                        children=[
                            dbc.Col(
                                width=12,
                                children=html.Div(
                                    children=premium_content_icon
                                ),
                            )
                        ],
                    ),

                    ],
                ),

            ]
        ),
    )

    return content