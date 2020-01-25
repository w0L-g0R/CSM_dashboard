# NAVBAR TABS
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from assets.styles import *

tabs = dcc.Tabs(
    vertical=True,
    mobile_breakpoint=1600,
    style=tab_component_styles,
    id="nav-tabs",
    value="tab-1",
    children=[
        dcc.Tab(
            label="Key Facts",
            value="tab-1",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Basic Metrics",
            value="tab-2",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Customer Segmentation",
            value="tab-3",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Customer Lifetime Value",
            value="tab-4",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Churn Prediction",
            value="tab-5",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Next Purchase Day Prediction",
            value="tab-6",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Market Response Models",
            value="tab-7",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Sales Prediction",
            value="tab-8",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="Uplift Modelling",
            value="tab-9",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
        dcc.Tab(
            label="A/B Testing Design",
            value="tab-10",
            style=tab_style,
            selected_style=tab_selected_style,
        ),
    ],
)

# NAVBAR TAB BOX
tabs_box = html.Div(children=tabs)

# NAVBAR TOOLTIPS
navbar_tooltips = html.Div(
    children=[
        dbc.Tooltip("Print", target="printer-icon"),
        dbc.Tooltip("Share", target="share-icon"),
        dbc.Tooltip("Logout", target="logout-icon"),
    ]
)

# ACTIVE USER CARD
active_user_card = dbc.Card(
    style=active_user_card_style,
    children=[
        dbc.CardBody(
            style=active_user_card_body_style,
            children=[
                dbc.Row(
                    no_gutters=True,
                    children=[
                        # ACTIVE USER ICON
                        dbc.Col(
                            width=12,
                            children=[
                                # OUTER CIRCLE
                                html.Div(
                                    style={
                                        "display": "block",
                                        "width": 66,
                                        "height": 66,
                                        "border-radius": 56,
                                        "border": "2px rgba(173, 216, 230, 0.3) solid",
                                        "margin": "auto",
                                    },
                                    children=[
                                        # ICON IMAGE
                                        html.I(
                                            className="fas fa-user",
                                            style={
                                                "background": "rgba(255, 0, 0, 0)",
                                                "color": "lightblue",
                                                "font-size": 40,
                                                "margin-top": "12%",
                                            },
                                        )
                                    ],
                                )
                            ],
                        ),
                        # ACTIVE USER MARKDOWN
                        dbc.Col(
                            width=12,
                            children=[
                                dbc.Row(
                                    no_gutters=True,
                                    children=[
                                        # TITLE
                                        dbc.Col(
                                            width=12,
                                            children=html.H6(
                                                children="Active User",
                                                className="card-title",
                                                style={
                                                    "color": "rgba(173, 216, 230, 0.3)",
                                                    "margin-top": 15,
                                                },
                                            ),
                                        ),
                                        # USER NAME
                                        dbc.Col(
                                            width=12,
                                            children=html.P(
                                                children="Foo",
                                                style={
                                                    "color": "lightblue",
                                                    "font-size": 20,
                                                    "margin-top": -12,
                                                    "margin-bottom": -5,
                                                },
                                            ),
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
        dbc.CardFooter(
            children=[
                dbc.Row(
                    no_gutters=True,
                    children=[
                        dbc.Col(
                            width=4,
                            children=[
                                # PRINTER ICON
                                html.I(
                                    id="printer-icon",
                                    className="fas fa-print",
                                    style=active_user_card_footer_icons,
                                )
                            ],
                        ),
                        dbc.Col(
                            width=4,
                            children=[
                                # SHARE ICON
                                html.I(
                                    id="share-icon",
                                    className="fas fa-share-alt",
                                    style=active_user_card_footer_icons,
                                )
                            ],
                        ),
                        dbc.Col(
                            width=4,
                            children=[
                                # LOGOUT ICON
                                html.I(
                                    id="logout-icon",
                                    className="fas fa-sign-out-alt",
                                    style=active_user_card_footer_icons,
                                )
                            ],
                        ),
                    ],
                )
            ]
        ),
    ],
)

# ACTIVE USER BOX
active_user_box = html.Div(style=active_user_box, children=[active_user_card])

brand = html.Img(
    src="https://fontmeme.com/permalink/200119/8b3d419c5667b8b36f59be82471eafef.png",
    style=navbar_logo_style,
)

brand_subtitle = html.Div(
    children="customer success management", style=navbar_logo_subtitle_style
)


# NAVBAR
navbar = dbc.Col(
    xs=12,
    sm=12,
    md=12,
    lg=12,
    xl=2,
    width={"offset": 0},
    style=navbar_background_style,
    children=[
        # BRAND
        brand,
        # SUBTITLE
        brand_subtitle,
        # TABS
        tabs_box,
        # ACTIVE USER BOX
        active_user_box,
        # NAVBAR TOOLTIPS
        navbar_tooltips,
    ],
)
