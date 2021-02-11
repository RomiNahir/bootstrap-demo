
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from pages import contact, login, components1, components2,map
from app import server

 #, , , DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI

items= [dbc.DropdownMenuItem("CERULEAN"),
        dbc.DropdownMenuItem("COSMO"),
        dbc.DropdownMenuItem("CYBORG"),
        dbc.DropdownMenuItem("JOURNAL"),
        dbc.DropdownMenuItem("LITERA"),
        dbc.DropdownMenuItem("LUMEN"),
        dbc.DropdownMenuItem("LUX"),
        dbc.DropdownMenuItem("MATERIA"),
        dbc.DropdownMenuItem("MINTY")
        ]

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(id="input-on-search",
                          type="text", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", id='search-val', n_clicks=0,
                       className="ml-2 btn-secondary btn"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dcc.Link(html.I(id='home-button', n_clicks=0, className='fa fa-home',
                                                style={'color': 'white', 'fontSize': '2rem'}), href='/')),
                        dbc.Col(dbc.NavbarBrand(
                            "Dash App Template", className="ml-2")),
                        dbc.DropdownMenu(
                        label="Themes",
                        children=items,)    
                    ],
                    align="center",
                    className="ml-auto flex-nowrap mt-3 mt-md-0",
                    no_gutters=True,
                ),
            ),

            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [search_bar], className="ml-auto", navbar=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ],
        fluid=True,
    ),
    color="#2c6693",
    dark=True,
)


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 60,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f4f6f8",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


link = [dbc.NavLink("1. Components", href="/components1", active="exact", style={"font-size": "19px", "padding-left": "0px"}),
        dbc.NavLink("2. Components", href="/components2", active="exact", style={"font-size": "19px", "padding-left": "0px"}),
        dbc.NavLink("Map", href="/map", active="exact",
                    style={"font-size": "19px", "padding-left": "0px"})
        ]

buttons = [dbc.Button("Contact Form", color="info", href='/contact', className="mr-1 btn-space"),
           ]


sidebar = html.Div(
    [
        html.H2("Dash Sidebar", className="display-8"),
        html.Hr(),
        html.P(
            "Example Pages", className="lead"
        ),
        dbc.Nav(link + buttons, vertical=True),
    ],
    style=SIDEBAR_STYLE,
    id="sidebar",
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), navbar, sidebar, content])


def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


def set_navitem_class(is_open):
    if is_open:
        return "open"
    return ""


for i in [1, 2]:
    app.callback(
        Output(f"submenu-{i}-collapse", "is_open"),
        [Input(f"submenu-{i}", "n_clicks")],
        [State(f"submenu-{i}-collapse", "is_open")],
    )(toggle_collapse)

    app.callback(
        Output(f"submenu-{i}", "className"),
        [Input(f"submenu-{i}-collapse", "is_open")],
    )(set_navitem_class)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return login.layout
    elif pathname == "/map":
        return map.layout
    elif pathname == '/contact':
        return contact.layout
    elif pathname == '/components1':
        return components1.layout
    elif pathname == '/components2':
        return components2.layout    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output("modal-centered", "is_open"),
    [Input("loginButton", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
