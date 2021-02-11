import dash_bootstrap_components as dbc
import dash_core_components as dcc

import dash_html_components as html
import plotly.express as px

from app import app
import pandas as pd


df2 = pd.DataFrame(
    {
        "First Name": ["Romina", "Mariano"],
        "Last Name": ["Mezher", "Giardina"],
    }
)

df = px.data.tips()


card_content = [
    dbc.CardHeader("Card header"),
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

layout = html.Div(
    [
        html.H1(children="Cards"),
        dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="primary", inverse=True)),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Card 1", className="card-title"),
                                html.P(
                                    "This card has some text content, which is a little "
                                    "bit longer than the second card.",
                                    className="card-text",
                                ),
                                dbc.Button(
                                    "Click here", color="success", className="mt-auto"
                                ),
                            ]
                        )
                    )
                ),
                dbc.Col(dbc.Card(
                    [
                        dbc.CardImg(
                            src="https://dash-bootstrap-components.opensource.faculty.ai/static/images/placeholder286x180.png", top=True),
                        dbc.CardBody(
                            [
                                html.H4("Card title", className="card-title"),
                                html.P(
                                    "Some quick example text to build on the card title and "
                                    "make up the bulk of the card's content.",
                                    className="card-text",
                                ),
                                dbc.Button("Go somewhere", color="primary"),
                            ]
                        ),
                    ],
                    style={"width": "18rem"})),
            ],
            className="mb-4",
        ),
        html.Hr(),
        html.H1(children="Charts"),
        dbc.Row(
            [dcc.Graph(id="pie-chart", figure=px.pie(df, values='tip', names='day')),
             dcc.Graph(id="historgram", figure=px.histogram(df, x="total_bill"))],
            className="mb-2",
        ),
        html.Hr(),
        html.H1(children="Dark Styled table"),
        dbc.Table.from_dataframe(
            df2, striped=True, bordered=True, hover=True, dark=True),
        html.Hr(),
        html.H1(children="Badges"),
        html.Span(
            [
                dbc.Badge("Primary", href="#",
                          color="primary", className="mr-1"),
                dbc.Badge("Secondary", href="#",
                          color="secondary", className="mr-1"),
                dbc.Badge("Success", href="#",
                          color="success", className="mr-1"),
                dbc.Badge("Warning", href="#",
                          color="warning", className="mr-1"),
                dbc.Badge("Danger", href="#",
                          color="danger", className="mr-1"),
                dbc.Badge("Info", href="#", color="info", className="mr-1"),
                dbc.Badge("Light", href="#", color="light", className="mr-1"),
                dbc.Badge("Dark", href="#", color="dark"),
            ]),
        html.Hr(),
        html.H1(children="Styled alerts"),
        html.Div(
            [
                dbc.Alert("This is a primary alert", color="primary"),
                dbc.Alert("This is a secondary alert", color="secondary"),
                dbc.Alert("This is a success alert! Well done!",
                          color="success"),
                dbc.Alert("This is a warning alert... be careful...",
                          color="warning"),
                dbc.Alert("This is a danger alert. Scary!", color="danger"),
                dbc.Alert("This is an info alert. Good to know!", color="info"),
                dbc.Alert("This is a light alert", color="light"),
                dbc.Alert("This is a dark alert", color="dark"),
            ]),
        html.Hr(),
        html.H1(children="Styled table"),
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
    ]
)
