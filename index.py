
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app
from pages import contact, login, components1, components2, tablepage,canvaspage,map
from app import server


# , , , DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI


def update_layout(value):
    if value:
        return([html.Link(href=value, rel='stylesheet')
                ])
    else:
        return([html.Link(href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css', rel='stylesheet')
                ])


search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(id="input-on-search",
                          type="text", placeholder="Search")),
        dbc.Col(
            children=[
                dbc.Button(
                    "Search", id="positioned-toast-toggle", className="ml-2 btn-primary btn"
                ),
                dbc.Toast(
                    "Your search result will be displayed soon!",
                    id="positioned-toast",
                    header="This is a Toast",
                    is_open=False,
                    dismissable=True,
                    icon="success",
                    # top: 66 positions the toast below the navbar
                    style={"position": "fixed", "top": 66,
                           "right": 10, "width": 350},
                )],
            width="auto"
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
                        dbc.Col(dcc.Link(html.I(id='home-button', n_clicks=0, className='fa fa-amazon',
                                                style={'color': 'white', 'fontSize': '2rem'}), href='/')),
                        dbc.Col(dbc.NavbarBrand(
                            "AWS Dash Template vBeta by Romina Mezher", className="ml-2"))
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
    "top": 120,
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


link = [dbc.NavLink("1. Components", href="/components1", active="exact", 
                    style={"font-size": "19px", "padding-left": "0px"}),
        dbc.NavLink("2. Components", href="/components2", active="exact",
                    style={"font-size": "19px", "padding-left": "0px"}),
        dbc.NavLink("3. Data Table", href="/tablepage", active="exact",
                    style={"font-size": "19px", "padding-left": "0px"}),                    
        dbc.NavLink("4. Map", href="/map", active="exact",
                    style={"font-size": "19px", "padding-left": "0px"}),
        dbc.NavLink("5. Canvas", href="/canvaspage", active="exact",
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
app.layout = html.Div([dcc.Dropdown(
    id='theme-dropdown',
    options=[
        {'label': 'CERULEAN', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cerulean/bootstrap.min.css'},
        {'label': 'COSMO', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cosmo/bootstrap.min.css'},
        {'label': 'CYBORG', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cyborg/bootstrap.min.css'},
        {'label': 'JOURNAL', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/journal/bootstrap.min.css'},
        {'label': 'LITERA', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/litera/bootstrap.min.css'},
        {'label': 'LUMEN', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/lumen/bootstrap.min.css'},
        {'label': 'MINTY', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/minty/bootstrap.min.css'},
        {'label': 'SANDSTONE', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/sandstone/bootstrap.min.css'},
        {'label': 'SIMPLEX', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/simplex/bootstrap.min.css'},
        {'label': 'SKETCHY', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/sketchy/bootstrap.min.css'},
        {'label': 'SOLAR', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/solar/bootstrap.min.css'},
        {'label': 'SPACELAB', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/spacelab/bootstrap.min.css'},
        {'label': 'SUPERHERO', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/superhero/bootstrap.min.css'},
        {'label': 'UNITED', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/united/bootstrap.min.css'},
        {'label': 'YETI', 'value': 'https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/yeti/bootstrap.min.css'},
    ], style={'margin': '10px 20px 10px 5px'}),
    html.Div([html.Div(id="style-layout"), dcc.Location(id="url"), navbar, sidebar, content])])


@app.callback(
    Output("style-layout", "children"),
    Input('theme-dropdown', 'value'),
)
def update_stylesheet(selectedTheme):
    return update_layout(selectedTheme)

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
    elif pathname == '/tablepage':
        return tablepage.layout 
    elif pathname == '/canvaspage':
        return canvaspage.layout                
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output("positioned-toast", "is_open"),
    [Input("positioned-toast-toggle", "n_clicks")],
)
def open_toast(n):
    if n:
        return True
    return False    


if __name__ == '__main__':
    app.run_server(debug=True)
