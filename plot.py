import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
import plotly.figure_factory as ff
import pandas as pd
import os

from plotly.subplots import make_subplots
from copy import deepcopy

"""####################################################################"""
"""                                 DATA                               """
"""####################################################################"""

# PICKLE DATA
df_revenues_growth = pd.read_pickle(path=os.getcwd() + "/data/df_revenues_growth.p")
df_customers_growth = pd.read_pickle(path=os.getcwd() + "/data/df_customers_growth.p")
df_orders_growth = pd.read_pickle(path=os.getcwd() + "/data/df_orders_growth.p")

df_new_customers_per_month = pd.read_pickle(
    path=os.getcwd() + "/data/df_new_customers_per_month.p"
)
df_existing_customers_per_month = pd.read_pickle(
    path=os.getcwd() + "/data/df_existing_customers_per_month.p"
)
df_revenues_new_customers = pd.read_pickle(
    path=os.getcwd() + "/data/df_revenues_new_customers.p"
)
df_revenues_existing_customers = pd.read_pickle(
    path=os.getcwd() + "/data/df_revenues_existing_customers.p"
)
df_orders_new_customers = pd.read_pickle(
    path=os.getcwd() + "/data/df_orders_new_customers.p"
)
df_orders_existing_customers = pd.read_pickle(
    path=os.getcwd() + "/data/df_orders_existing_customers.p"
)

df_retention_monthly = pd.read_pickle(path=os.getcwd() + "/data/df_retention_monthly.p")
df_retention_cohort = pd.read_pickle(path=os.getcwd() + "/data/df_retention_cohort.p")
df_customers_per_country = pd.read_pickle(
    path=os.getcwd() + "/data/df_customers_per_country.p"
)

df_total_score_table = pd.read_pickle(path=os.getcwd() + "/data/df_total_score_table.p")
df_customer_segments = pd.read_pickle(path=os.getcwd() + "/data/df_customer_segments.p")

LV_recency = df_customer_segments.query("Segment == 'Low-Value'")["Recency"]
LV_frequency = df_customer_segments.query("Segment == 'Low-Value'")["Frequency"]
LV_revenues = df_customer_segments.query("Segment == 'Low-Value'")["Revenue"]

MV_recency = df_customer_segments.query("Segment == 'Mid-Value'")["Recency"]
MV_frequency = df_customer_segments.query("Segment == 'Mid-Value'")["Frequency"]
MV_revenues = df_customer_segments.query("Segment == 'Mid-Value'")["Revenue"]

HV_recency = df_customer_segments.query("Segment == 'High-Value'")["Recency"]
HV_frequency = df_customer_segments.query("Segment == 'High-Value'")["Frequency"]
HV_revenues = df_customer_segments.query("Segment == 'High-Value'")["Revenue"]

df_recency_cluster_1 = df_customer_segments.query("RecencyCluster == 0")["Recency"]
df_recency_cluster_2 = df_customer_segments.query("RecencyCluster == 1")["Recency"]
df_recency_cluster_3 = df_customer_segments.query("RecencyCluster == 2")["Recency"]
df_recency_cluster_4 = df_customer_segments.query("RecencyCluster == 3")["Recency"]

df_frequency_cluster_1 = df_customer_segments.query("FrequencyCluster == 0")[
    "Frequency"
]
df_frequency_cluster_2 = df_customer_segments.query("FrequencyCluster == 1")[
    "Frequency"
]
df_frequency_cluster_3 = df_customer_segments.query("FrequencyCluster == 2")[
    "Frequency"
]
df_frequency_cluster_4 = df_customer_segments.query("FrequencyCluster == 3")[
    "Frequency"
]

df_revenue_cluster_1 = df_customer_segments.query("RevenueCluster == 0")["Revenue"]
df_revenue_cluster_2 = df_customer_segments.query("RevenueCluster == 1")["Revenue"]
df_revenue_cluster_3 = df_customer_segments.query("RevenueCluster == 2")["Revenue"]
df_revenue_cluster_4 = df_customer_segments.query("RevenueCluster == 3")["Revenue"]

sales_stats = pd.read_pickle(path=os.getcwd() + "/data/sales_stats_feb_to_nov.p")

month_names = ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]

"""####################################################################"""
"""                              MONTHLY                               """
"""####################################################################"""


def monthly(customers: bool = None, orders: bool = None, revenues: bool = None):

    """ Pass either revenues or number of customers series per month, depending on boolean flag """

    fig = make_subplots(
        rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.16, row_heights=[0.7, 0.3]
    )

    # CUSTOMERS
    if customers:
        new_customer_data = df_new_customers_per_month
        existing_customer_data = df_existing_customers_per_month
        growth_rates_data = df_customers_growth
        new_customer_color = "#45A29E"
        existing_customer_color = "#66FCF1"

    # ORDERS
    elif orders:
        new_customer_data = df_orders_new_customers
        existing_customer_data = df_orders_existing_customers
        growth_rates_data = df_orders_growth
        new_customer_color = "#D79922"
        existing_customer_color = "#EFE2BA"

    # REVENUES
    elif revenues:
        new_customer_data = df_revenues_new_customers
        existing_customer_data = df_revenues_existing_customers
        growth_rates_data = df_revenues_growth
        new_customer_color = "#ADADAD"
        existing_customer_color = "#64485C"

    else:
        raise AttributeError("Input error!")

    # MARKER COLORSCALE
    rates = growth_rates_data
    rates.index = month_names
    c = [0 if value <= 0 else 1 for value in rates]

    # EXISTING
    fig.append_trace(
        go.Bar(
            x=month_names,
            y=existing_customer_data,
            name="Existing Customers",
            marker_color=existing_customer_color,
            marker_line_color="black",
            marker_line_width=1.5,
            opacity=0.6,
        ),
        row=1,
        col=1,
    )

    # NEW
    fig.append_trace(
        go.Bar(
            x=month_names,
            y=new_customer_data,
            name="New Customers",
            marker_color=new_customer_color,
            marker_line_color="black",
            marker_line_width=1.5,
            opacity=0.6,
        ),
        row=1,
        col=1,
    )

    # GROWTH
    fig.append_trace(
        go.Scatter(
            x=rates.index,
            y=rates * 100,
            name="Growth rate (%)",
            mode="lines+markers",
            line=dict(width=1, color="lightblue"),
            marker=dict(
                size=7,
                color=c,
                symbol="diamond",
                colorscale=[[0, "red"], [1, "limegreen"]],
                line=dict(width=0.4, color="black"),
            ),
            xaxis="x2",
            yaxis="y2",
            showlegend=True,
        ),
        row=2,
        col=1,
    )

    fig.update_layout(
        barmode="stack",
        font=dict(family="Oswald Light, sans-serif", size=12, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=288,
        margin=dict(l=40, r=20, t=0, b=0, pad=0),
        xaxis=dict(
            type="category",
            mirror=True,
            autorange=True,
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
        ),
        yaxis=dict(
            mirror="all",
            autorange=True,
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
            gridwidth=0.5,
            gridcolor="rgba(173, 216, 230, 0.2)",
            zerolinewidth=1,
        ),
        xaxis2=dict(
            autorange=True,
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
            showgrid=False,
            side="top",
            tickcolor="rgba(0, 0, 0, 0)",
            ticklen=15,
            ticks="outside",
            tickwidth=2,
        ),
        yaxis2=dict(
            range=[-25, 60],
            hoverformat=".2f",
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
            ticksuffix="%",
            showgrid=True,
            side="left",
            gridwidth=0.5,
            gridcolor="rgba(173, 216, 230, 0.2)",
            zeroline=False,
        ),
        showlegend=True,
        legend=go.layout.Legend(
            x=-0.08,
            y=0,
            font=dict(family="Oswald Extra Light, sans-serif", size=10, color="white"),
            bgcolor="rgba(255,0,0,0)",
            orientation="h",
        ),
    )

    return dcc.Graph(figure=fig)


"""####################################################################"""
"""                              RETENTION                             """
"""####################################################################"""


def retention_monthly():
    fig = go.Figure(
        data=go.Barpolar(
            r=df_retention_monthly["RetentionRate"],
            theta=month_names,
            marker_color="lime",
            width=[x for x in df_retention_monthly["RetentionRate"]],
            marker_line_color="lightblue",
            marker_line_width=1,
            opacity=0.3,
        )
    )

    fig.update_layout(
        font=dict(family="Oswald Light, sans-serif", size=14, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=280,
        margin=dict(l=0, r=0, t=35, b=25, pad=0),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 0.5],
                tickfont=dict(size=10, color="white"),
                tickangle=45,
            )
        ),
        showlegend=False,
        template="plotly_dark",
    )

    return dcc.Graph(figure=fig)


"""####################################################################"""
"""                              COHORT                                """
"""####################################################################"""


def retention_cohort():

    z_strings = deepcopy(df_retention_cohort)

    for column_index, value in z_strings.items():
        z_strings[column_index] = z_strings[column_index].map(
            lambda x: str(int(x * 100)) + "%" if not pd.isna(x) else ""
        )

    z_strings.fillna("", inplace=True)
    z_strings = z_strings[z_strings.columns].values

    z = df_retention_cohort[df_retention_cohort.columns].values

    x = month_names
    y = month_names

    font_colors = ["lightblue", "black"]

    fig = ff.create_annotated_heatmap(
        z,
        x=x,
        y=y,
        colorscale="algae",
        font_colors=font_colors,
        annotation_text=z_strings,
    )

    fig.update_yaxes(autorange="reversed")
    fig.update_layout(
        font=dict(family="Oswald Light, sans-serif", size=12, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=260,
        margin=dict(l=50, r=25, t=40, b=0, pad=0),
        template="plotly_dark",
    )

    return dcc.Graph(figure=fig)


"""####################################################################"""
"""                              MAP                                   """
"""####################################################################"""


def map_graph(
    locations: pd.DataFrame,
    z: pd.DataFrame,
    text: pd.DataFrame,
    customdata: pd.DataFrame,
    hovertemplate: str,
):

    fig = go.Figure(
        data=go.Choropleth(
            locations=locations,
            z=z,
            text=text,
            colorscale="viridis",
            customdata=customdata,
            hovertemplate=hovertemplate,
            autocolorscale=False,
            reversescale=True,
            marker_line_color="darkgray",
            marker_line_width=0.5,
            showscale=False,
        )
    )

    fig.update_layout(
        font=dict(family="Oswald Light, sans-serif", size=12, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=265,
        showlegend=True,
        geo={
            "bgcolor": "black",
            "showcountries": False,
            "showlakes": False,
            "showframe": False,
            "oceancolor": "black",
            "landcolor": "rgba(173, 216, 230, 0.3)",
            "countrycolor": "rgba(173, 216, 230, 0.3)",
            "projection_type": "natural earth",
        },
        margin={"t": 0, "l": 0, "b": 0, "r": 0},
    )

    return fig


"""####################################################################"""
"""                            RFM HISTO                               """
"""####################################################################"""


def rfm_histogram(
    recency: bool = False, frequency: bool = False, monetary: bool = False
):

    if recency:
        data = df_customer_segments["Recency"]
        name = "Recency Distribution"
        x_axis_title = "Inactive Days"
        bin_color = "#66FCF1"
        value_range = [0, 340]

    elif frequency:
        data = df_customer_segments["Frequency"]
        name = "Frequency Distribution"
        x_axis_title = "Orders"
        bin_color = "#EFE2BA"
        value_range = [0, 500]

    elif monetary:
        data = df_customer_segments["Revenue"]
        name = "Revenues Distribution"
        x_axis_title = "Euro"
        bin_color = "coral"
        value_range = [0, 10000]

    fig = go.Figure(
        go.Histogram(
            x=data,
            histfunc="count",
            name=name,
            marker={"line": {"color": "black", "width": 0.2}},
            marker_color=bin_color,
            opacity=0.6,
            xbins={"start": 0.5},
        )
    )

    fig.update_layout(

        font=dict(family="Oswald Light, sans-serif", size=14, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=280,
        margin=dict(l=60, r=30, t=5, b=10, pad=0),
        xaxis=dict(
            range=value_range,
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
            title=x_axis_title,
        ),
        yaxis=dict(
            mirror="all",
            autorange=True,
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
            gridwidth=0.5,
            gridcolor="rgba(173, 216, 230, 0.2)",
            zerolinewidth=1,
            title="Customers",
            ticklen=2,
            ticks="outside",
            tickwidth=2,
        ),
        showlegend=True,
        legend=go.layout.Legend(
            font=dict(family="Oswald Light, sans-serif", size=14, color="lightblue"),
            x=0.65,
            y=1,
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
        ),
    )

    return fig


"""####################################################################"""
"""                          RFM CLUSTER                               """
"""####################################################################"""


def cluster_boxplots(
    recency: bool = False, frequency: bool = False, monetary: bool = False
):

    if recency:
        y = [
            df_recency_cluster_1,
            df_recency_cluster_2,
            df_recency_cluster_3,
            df_recency_cluster_4,
        ]
        y_axis_title = "Days"
        color = "#25cec4"

    elif frequency:
        y = [
            df_frequency_cluster_1,
            df_frequency_cluster_2,
            df_frequency_cluster_3,
            df_frequency_cluster_4,
        ]
        y_axis_title = "Orders"
        color = "#EFE2BA"

    elif monetary:
        y = [
            df_revenue_cluster_1,
            df_revenue_cluster_2,
            df_revenue_cluster_3,
            df_revenue_cluster_4,
        ]
        y_axis_title = "Euro"
        color = "coral"

    fig = go.Figure()

    fig.add_trace(
        go.Box(
            y=y[0],
            name="Cluster 1",
            boxmean="sd",
            fillcolor="rgba(0,0,0,0)",
            line_color=color,
            line_width=1.25,
        )
    )

    fig.add_trace(
        go.Box(
            y=y[1],
            name="Cluster 2",
            boxmean="sd",
            fillcolor="rgba(0,0,0,0)",
            line_color=color,
            line_width=1.25,
        )
    )

    fig.add_trace(
        go.Box(
            y=y[2],
            name="Cluster 3",
            boxmean="sd",
            fillcolor="rgba(0,0,0,0)",
            line_color=color,
            line_width=1.25,
        )
    )

    fig.add_trace(
        go.Box(
            y=y[3],
            name="Cluster 4",
            boxmean="sd",
            fillcolor="rgba(0,0,0,0)",
            line_color=color,
            line_width=1.25,
        )
    )

    fig.update_layout(
        font=dict(family="Oswald Light, sans-serif", size=14, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=220,
        margin=dict(l=60, r=30, t=5, b=10, pad=0),
        xaxis=dict(showline=False, linewidth=1, linecolor="rgba(173, 216, 230, 0.3)"),
        yaxis=dict(
            mirror="all",
            autorange=True,
            showline=False,
            linewidth=1,
            linecolor="rgba(173, 216, 230, 0.3)",
            gridwidth=0.5,
            gridcolor="rgba(173, 216, 230, 0.2)",
            zerolinewidth=1,
            title=y_axis_title,
        ),
        showlegend=False,
    )

    return fig


import numpy as np

"""####################################################################"""
"""                              SEGMENTS 3D                           """
"""####################################################################"""


def segments_3D():

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=df_customer_segments.query("Segment == 'Low-Value'")["Recency"],
                z=df_customer_segments.query("Segment == 'Low-Value'")["Revenue"],
                y=df_customer_segments.query("Segment == 'Low-Value'")["Frequency"],
                name="Low-Value-Segment",
                hovertemplate="<br>Recency:%{x}<br>Frequency:%{y}<br>Revenue: %{z}<extra></extra>",
                mode="markers",
                marker=dict(size=6, color="red", opacity=0.8),
            ),
            go.Scatter3d(
                x=df_customer_segments.query("Segment == 'Mid-Value'")["Recency"],
                z=df_customer_segments.query("Segment == 'Mid-Value'")["Revenue"],
                y=df_customer_segments.query("Segment == 'Mid-Value'")["Frequency"],
                name="Mid-Value-Segment",
                mode="markers",
                hovertemplate="<br>Recency:%{x}<br>Frequency:%{y}<br>Revenue: %{z}<extra></extra>",
                marker=dict(size=6, color="green", opacity=0.8),
            ),
            go.Scatter3d(
                x=df_customer_segments.query("Segment == 'High-Value'")["Recency"],
                z=df_customer_segments.query("Segment == 'High-Value'")["Revenue"],
                y=df_customer_segments.query("Segment == 'High-Value'")["Frequency"],
                name="High-Value-Segment",
                hovertemplate="<br>Recency:%{x}<br>Frequency:%{y}<br>Revenue: %{z}<extra></extra>",
                mode="markers",
                marker=dict(size=6, color="blue", opacity=0.8),
            ),
        ]
    )

    fig.update_layout(
        font=dict(family="Oswald Light, sans-serif", size=12, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=400,
        margin=dict(l=0, r=0, b=0, t=0),
        template="plotly_dark",
        legend=go.layout.Legend(
            font=dict(family="Oswald Light, sans-serif", size=14, color="lightblue"),
            x=0.2,
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
        ),
        scene={
            "aspectmode": "auto",
            "xaxis": {"title": "Recency (Days)"},
            "zaxis": {"title": "Revenues (Euros)"},
            "yaxis": {"title": "Frequency (Orders)"},
        },
        scene_camera=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=-0.1),
            eye=dict(x=1.5, y=1.5, z=0.1),
        ),
    )

    return dcc.Graph(figure=fig)


"""####################################################################"""
"""                              TREEMAP                               """
"""####################################################################"""


def segments_treemap():

    labels = [
        "Low-Value-Segment",
        "L1",
        "L2",
        "L3",
        "Mid-Value-Segment",
        "M1",
        "M2",
        "M3",
        "High-Value-Segment",
        "H1",
        "H2",
        "H3",
    ]
    parents = [
        "",
        "Low-Value-Segment",
        "Low-Value-Segment",
        "Low-Value-Segment",
        "",
        "Mid-Value-Segment",
        "Mid-Value-Segment",
        "Mid-Value-Segment",
        "",
        "High-Value-Segment",
        "High-Value-Segment",
        "High-Value-Segment",
    ]

    text = [
        ["", "", ""],
        [
            df_total_score_table.loc[0, "Recency"],
            df_total_score_table.loc[0, "Frequency"],
            df_total_score_table.loc[0, "Revenue"],
        ],
        [
            df_total_score_table.loc[1, "Recency"],
            df_total_score_table.loc[1, "Frequency"],
            df_total_score_table.loc[1, "Revenue"],
        ],
        [
            df_total_score_table.loc[2, "Recency"],
            df_total_score_table.loc[2, "Frequency"],
            df_total_score_table.loc[2, "Revenue"],
        ],
        ["", "", ""],
        [
            df_total_score_table.loc[3, "Recency"],
            df_total_score_table.loc[3, "Frequency"],
            df_total_score_table.loc[3, "Revenue"],
        ],
        [
            df_total_score_table.loc[4, "Recency"],
            df_total_score_table.loc[4, "Frequency"],
            df_total_score_table.loc[4, "Revenue"],
        ],
        [
            df_total_score_table.loc[5, "Recency"],
            df_total_score_table.loc[5, "Frequency"],
            df_total_score_table.loc[5, "Revenue"],
        ],
        ["", "", ""],
        [
            df_total_score_table.loc[6, "Recency"],
            df_total_score_table.loc[6, "Frequency"],
            df_total_score_table.loc[6, "Revenue"],
        ],
        [
            df_total_score_table.loc[7, "Recency"],
            df_total_score_table.loc[7, "Frequency"],
            df_total_score_table.loc[7, "Revenue"],
        ],
        [
            df_total_score_table.loc[8, "Recency"],
            df_total_score_table.loc[8, "Frequency"],
            df_total_score_table.loc[8, "Revenue"],
        ],
    ]

    textinfo = "label+text"

    fig = go.Figure(
        go.Treemap(
            labels=labels,
            parents=parents,
            text=text,
            textinfo=textinfo,
            textfont=dict(
                family="Oswald Light, sans-serif", size=14, color="lightblue"
            ),
            texttemplate="<b>%{label}-Customers</b><br>Recency:<br>%{text[0]} Days<br>Frequency:<br>%{text[1]} Orders<br>Revenues:<br>%{text[2]:,} €",
            hoverinfo="none",
        )
    )

    # tight layout
    fig.update_layout(
        font=dict(family="Oswald Light, sans-serif", size=14, color="lightblue"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        autosize=True,
        height=200,
        margin=dict(l=0, r=0, b=20, t=0),
        treemapcolorway=["darkred", "green", "blue"],
        annotations=[
            go.layout.Annotation(
                x=0.52,
                y=0.99,
                showarrow=False,
                text="[Average values]",
                xref="paper",
                yref="paper",
                font=dict(
                    family="Oswald Extra Light, sans-serif", color="white", size=11
                ),
            )
        ],
    )

    return dcc.Graph(figure=fig)


"""####################################################################"""
"""                            INDICATOR                               """
"""####################################################################"""


def indicator_plot(name: str):

    if "customers" in name:
        value = sales_stats["customers"]
        reference = value * 0.8
    if "countries" in name:
        value = sales_stats["countries"]
        reference = value * 0.9
    if "quantities" in name:
        value = sales_stats["quantity"]
        reference = value * 1.2
    if "orders" in name:
        value = sales_stats["orders"]
        reference = value * 1.03
    if "products" in name:
        value = sales_stats["products"]
        reference = value * 0.77
    if "revenues" in name:
        value = round(sales_stats["revenues"])
        reference = value * 0.69

    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            mode="number+delta",
            value=value,
            title={
                "text": name,
                "font": dict(
                    family="Oswald Light, sans-serif", size=18, color="lightblue"
                ),
            },
            delta={"reference": reference, "relative": True},
            domain={"x": [0.25, 0.75], "y": [0.25, 0.75]},
            number={
                "font": {
                    "family": "Oswald Light, sans-serif",
                    "size": 32,
                    "color": "white",
                }
            },
        )
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=120,
        width=120,
        margin=dict(l=0, r=0, b=0, t=10),
    )

    return dcc.Graph(figure=fig)
