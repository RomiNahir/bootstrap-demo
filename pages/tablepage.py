import dash_table
import pandas as pd
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_core_components as dcc
import plotly.express as px

from app import app

filename = 'data.csv'

originaldf = pd.read_csv(filename, sep=';', header=0, usecols=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
                       names=['Station Name', 'lat', 'lon', 'Air Temperature', 'Dew Point Temperature', 'Wind Direction', 'Wind Speed', 'Pressure',
                       'Precipitation', 'Cloud Fraction'],
                       na_values=-99999)


Variables = {
    "Dew Point [ºC]": "Dew Point Temperature",
    "Temperature [ºC]": "Air Temperature",
    "Precipitation [mm]": "Precipitation",
    "Pressure [hPa]": "Pressure",
    "Cloud Cover": "Cloud Fraction",
    "Wind Direction [deg]": "Wind Direction",
    "Wind Speed [km/h]": "Wind Speed",
}

Relations = {
    4: "Dew Point Temperature",
    3: "Air Temperature",
    8: "Precipitation",
    7: "Pressure",
    9: "Cloud Fraction",
    5: "Wind Direction",
    6: "Wind Speed",
}


def update_datatable(value):

    key = list(Relations.keys())[list(Relations.values()).index(value)]
    df = pd.read_csv('data.csv', sep=';', header=0, usecols=(0, key),
                       names=['Station Name', value],
                       na_values=-99999)

    return([
        html.H2("Weather Data Table"),
        dash_table.DataTable(
            id='table-paging-and-sorting', columns=[{'name': i, 'id': i, 'deletable': True} for i in df.columns],
            sort_action="native",
            page_action="native",
            page_current= 0,
            page_size= 15,            
            # Con style header estilamos el encabezado de la tabla (CSS)
            style_header={
                'backgroundColor': '#336699',
                'textAlign': 'left',
                'padding': '5px',
                'color': '#fff',
                'font-weight': 'bold'
            },
            # Con style cell estimamos las celdas de la tabla (CSS)
            style_cell={
                'backgroundColor': '#fff',
                'color': '#000',
                'textAlign': 'center',
                'font-family': 'Helvetica',
                'font-size': '13px',
            },
            # # Importante aca, hay que sumarle la propiedad data al momento del nacimiento de la dataTable
            data=df.to_dict('records'),
        )
    ])


layout = html.Div(
    children=[
        html.Div(className="row",
            children=[
                html.Div(className="eight columns",
                    children=[html.H2("Weather Data Map"),
                    html.P("""Select variable"""),
                                html.Div(
                                    children=[
                                        # Dropdown for locations on map
                                        dcc.Dropdown(
                                            id="variable-dropdown",
                                            options=[
                                                {"label": key, "value": value} for key, value in Variables.items()],
                                                    value="Air Temperature",
                                        )
                                    ],
                                ),
                                html.Div(
                                    children=[
                                        dcc.Graph(id="graph")
                                        ])
                    ]
                ),
                html.Div(className="four columns", id="data-table")
            ]
        )
    ]
)

# Update Map Graph
@app.callback(
    Output("graph", "figure"),
    [
        Input("variable-dropdown", "value"),
    ],
)
def update_graph(value):
    if value:

        data = originaldf[["lat", "lon", value]]

        fig = px.scatter_mapbox(data, lat="lat", lon="lon", color=value,
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=4, height=800)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.update_layout(coloraxis_colorbar=dict(thickness=20,
                           ticklen=3, tickcolor='black',
                           tickfont=dict(size=15, color='black')))

        fig.update_traces(marker=dict(size=14))

        return fig

# Update table
@app.callback(
     Output("data-table", "children"),
     Input("variable-dropdown", "value"))
def update_data(value):
    return update_datatable(value)