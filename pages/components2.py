import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import dash_html_components as html
import plotly.express as px

from app import app

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 1!", className="card-text"),
            dbc.Button("Click here", color="success"),
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This is tab 2!", className="card-text"),
            dbc.Button("Don't click here", color="danger"),
        ]
    ),
    className="mt-3",
)

layout = html.Div(
    [
        html.H1(children="InputGroup"),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon(dbc.Checkbox(), addon_type="prepend"),
                dbc.Input(),
            ]
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("@", addon_type="prepend"),
                dbc.Input(placeholder="Username"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.Input(placeholder="Recipient's username"),
                dbc.InputGroupAddon("@example.com", addon_type="append"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("$", addon_type="prepend"),
                dbc.Input(placeholder="Amount", type="number"),
                dbc.InputGroupAddon(".00", addon_type="append"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("With textarea", addon_type="prepend"),
                dbc.Textarea(),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.Select(
                    options=[
                        {"label": "Option 1", "value": 1},
                        {"label": "Option 2", "value": 2},
                    ]
                ),
                dbc.InputGroupAddon("With select", addon_type="append"),
            ]
        ),
        html.Hr(),
        html.H1(children="List Groups"),
        html.Div([dbc.Row(
            [dbc.Col(dbc.ListGroup(
                [
                    dbc.ListGroupItem("Active item", active=True),
                    dbc.ListGroupItem("Item 2", color="primary"),
                    dbc.ListGroupItem("Item 3", color="warning"),
                ]
            ), md=6),
                dbc.Col(dbc.ListGroup(
                    [
                        dbc.ListGroupItem("Contact", href="/contact"),
                        dbc.ListGroupItem(
                            "External link", href="https://aws.amazon.com/"),
                        dbc.ListGroupItem(
                            "Disabled link", href="https://aws.amazon.com/", disabled=True),
                    ]
                ), md=6),
            ],
        ),
        ]
        ),
        html.Hr(),
        html.H1(children="Modal"),

        dbc.Button("Small modal", id="open-sm",
                   className="mr-1", color="primary"),
        dbc.Button("Large modal", id="open-lg",
                   className="mr-1", color="success"),
        dbc.Button("Extra large modal", id="open-xl",
                   outline=True, color="danger"),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("A small modal."),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-sm",
                               className="ml-auto", color="primary")
                ),
            ],
            id="modal-sm",
            size="sm",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("A large modal."),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-lg",
                               className="ml-auto", color="success")
                ),
            ],
            id="modal-lg",
            size="lg",
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("An extra large modal."),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-xl",
                               className="ml-auto", outline=True, color="danger")
                ),
            ],
            id="modal-xl",
            size="xl",
        ),
        html.Hr(className="mb-3 mt-3"),
        html.H1(children="Tabs"),
        dbc.Tabs(
            [
                dbc.Tab(tab1_content, label="Tab 1"),
                dbc.Tab(tab2_content, label="Tab 2"),
                dbc.Tab(
                    "This tab's content is never seen", label="Tab 3", disabled=True
                ),
            ]),
        html.Hr(className="mb-5")
    ],
)


@ app.callback(Output("content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    elif at == "tab-2":
        return tab2_content
    return html.P("This shouldn't ever be displayed...")


def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


app.callback(
    Output("modal-sm", "is_open"),
    [Input("open-sm", "n_clicks"), Input("close-sm", "n_clicks")],
    [State("modal-sm", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-lg", "is_open"),
    [Input("open-lg", "n_clicks"), Input("close-lg", "n_clicks")],
    [State("modal-lg", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-xl", "is_open"),
    [Input("open-xl", "n_clicks"), Input("close-xl", "n_clicks")],
    [State("modal-xl", "is_open")],
)(toggle_modal)
