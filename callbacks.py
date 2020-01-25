import os
import pandas as pd
from dash.dependencies import Input, Output
from copy import deepcopy
from app import app

from plot import map_graph, rfm_histogram, cluster_boxplots


"""####################################################################"""
"""                         PER COUNTRY MAP                            """
"""####################################################################"""

df_customers_per_country = pd.read_pickle(
    path=os.getcwd() + "/data/df_customers_per_country.p"
)
customdata_customers = deepcopy(df_customers_per_country["TotalCustomer"])
df_customers_per_country.loc[0, "TotalCustomer"] /= 10

df_revenues_per_country = pd.read_pickle(
    path=os.getcwd() + "/data/df_revenues_per_country.p"
)
customdata_revenues = deepcopy(df_revenues_per_country["TotalRevenues"])
df_revenues_per_country.loc[0, "TotalRevenues"] /= 10


@app.callback(
    Output("per-country-map-graph", "figure"), [Input("map-radio-items", "value")]
)
def update_map_figure(value):

    # REVENUES
    if value == 1:
        fig = map_graph(
            locations=df_revenues_per_country["ISO"],
            z=df_revenues_per_country["TotalRevenues"],
            text=df_revenues_per_country["Country"],
            customdata=customdata_revenues,
            hovertemplate="<b>%{text}</b><br>%{customdata:.2s} €<extra></extra>",
        )

    # CUSTOMERS
    elif value == 2:
        fig = map_graph(
            locations=df_customers_per_country["ISO"],
            z=df_customers_per_country["TotalCustomer"],
            text=df_customers_per_country["Country"],
            customdata=customdata_customers,
            hovertemplate="<b>%{text}</b><br>%{customdata}<extra></extra>",
        )

    return fig


"""####################################################################"""
"""                             RFM FIGURES                            """
"""####################################################################"""


@app.callback(
    [Output("RFM-histogram-graph", "figure"), Output("RFM-boxplots-graph", "figure")],
    [Input("slider-histogram", "value")],
)
def update_rfm_figures(value):

    if value == 0:
        histogram_fig = rfm_histogram(recency=True)
        boxplot_fig = cluster_boxplots(recency=True)

    elif value == 1:
        histogram_fig = rfm_histogram(frequency=True)
        boxplot_fig = cluster_boxplots(frequency=True)

    elif value == 2:
        histogram_fig = rfm_histogram(monetary=True)
        boxplot_fig = cluster_boxplots(monetary=True)

    return histogram_fig, boxplot_fig
