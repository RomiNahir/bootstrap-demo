import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

#from flask_login import login_user
#from werkzeug.security import check_password_hash


layout = dbc.Container([
    html.Br(),
    dbc.Container([
        dcc.Location(id='urlLogin', refresh=True),
        html.Div([
            dbc.Container(children=[
                html.Img(
                    src='https://image.flaticon.com/icons/png/128/1077/1077114.png',
                    style={'float': 'right', 'width': '5%', 'margin-bottom' : '20px'}
                ),
                html.H2('Please sign in',
                        className='center'
                        )]
            ),
            dbc.Container(id='loginType', children=[
                dcc.Input(
                    placeholder='Enter your username',
                    type='text',
                    id='usernameBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                dcc.Input(
                    placeholder='Enter your password',
                    type='password',
                    id='passwordBox',
                    className='form-control',
                    n_submit=0,
                ),
                html.Br(),
                html.A(
                    href='/components1',
                    className='btn btn-primary btn-lg',
                    children='Login'
                ),
                html.Br(),
            ], className='form-group'),
        ]),
    ], className='jumbotron')
])


# @app.callback(Output('urlLogin', 'pathname'),
#                [Input('loginButton', 'n_clicks')
#                ])
# def sucess(n_clicks):
#     return '/home'

################################################################################
# LOGIN BUTTON CLICKED / ENTER PRESSED - REDIRECT TO PAGE1 IF LOGIN DETAILS ARE CORRECT
################################################################################
# @app.callback(Output('urlLogin', 'pathname'),
#               [Input('loginButton', 'n_clicks'),
#               Input('usernameBox', 'n_submit'),
#               Input('passwordBox', 'n_submit')],
#               [State('usernameBox', 'value'),
#                State('passwordBox', 'value')])
# def sucess(n_clicks, usernameSubmit, passwordSubmit, username, password):
#     user = User.query.filter_by(username=username).first()
#     if user:
#         if check_password_hash(user.password, password):
#             login_user(user)
#             return '/page1'
#         else:
#             pass
#     else:
#         pass


# ################################################################################
# # LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
# ################################################################################
# @app.callback(Output('usernameBox', 'className'),
#               [Input('loginButton', 'n_clicks'),
#               Input('usernameBox', 'n_submit'),
#               Input('passwordBox', 'n_submit')],
#               [State('usernameBox', 'value'),
#                State('passwordBox', 'value')])
# def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
#     if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
#         user = User.query.filter_by(username=username).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 return 'form-control'
#             else:
#                 return 'form-control is-invalid'
#         else:
#             return 'form-control is-invalid'
#     else:
#         return 'form-control'


# ################################################################################
# # LOGIN BUTTON CLICKED / ENTER PRESSED - RETURN RED BOXES IF LOGIN DETAILS INCORRECT
# ################################################################################
# @app.callback(Output('passwordBox', 'className'),
#               [Input('loginButton', 'n_clicks'),
#               Input('usernameBox', 'n_submit'),
#               Input('passwordBox', 'n_submit')],
#               [State('usernameBox', 'value'),
#                State('passwordBox', 'value')])
# def update_output(n_clicks, usernameSubmit, passwordSubmit, username, password):
#     if (n_clicks > 0) or (usernameSubmit > 0) or (passwordSubmit) > 0:
#         user = User.query.filter_by(username=username).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 return 'form-control'
#             else:
#                 return 'form-control is-invalid'
#         else:
#             return 'form-control is-invalid'
#     else:
#         return 'form-control'
