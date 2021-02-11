import plotly.express as px
import plotly.graph_objs as go

import geopandas as gpd
import dash_core_components as dcc
import dash_html_components as html

from app import app


geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))


fig = px.scatter_mapbox(geo_df, lat=geo_df.geometry.y, lon=geo_df.geometry.x, zoom=2, height=800,center=go.layout.mapbox.Center(
            lat=10,lon=-60
        ))

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(coloraxis_colorbar=dict(thickness=20,
                           ticklen=3, tickcolor='black',
                           tickfont=dict(size=15, color='black')))
fig.update_traces(marker=dict(size=14))

layout = html.Div([
            dcc.Graph(figure=fig)
        ]

)
