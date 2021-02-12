import dash
import dash_bootstrap_components as dbc


FA = "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"

app = dash.Dash(__name__, suppress_callback_exceptions=True,external_stylesheets=[FA])

app.title = 'AWS Dash Demo Template vBeta'

server = app.server


# # User management initialization
# from sqlalchemy import Table, create_engine
# from sqlalchemy.sql import select
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
# import sqlite3
# import warnings
# import os
# from flask_login import login_user, logout_user, current_user, LoginManager, UserMixin
# import configparser
# warnings.filterwarnings("ignore")
# conn = sqlite3.connect('data.sqlite')
# engine = create_engine('sqlite:///data.sqlite')
# db = SQLAlchemy()
# config = configparser.ConfigParser()
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(15), unique=True, nullable = False)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))
# Users_tbl = Table('users', Users.metadata)
# app = dash.Dash(__name__)
# server = app.server
# app.config.suppress_callback_exceptions = True
# # config
# server.config.update(
#     SECRET_KEY=os.urandom(12),
#     SQLALCHEMY_DATABASE_URI='sqlite:///data.sqlite',
#     SQLALCHEMY_TRACK_MODIFICATIONS=False
# )
# db.init_app(server)
# # Setup the LoginManager for the server
# login_manager = LoginManager()
# login_manager.init_app(server)
# login_manager.login_view = '/login'
# #User as base
# # Create User class with UserMixin
# class Users(UserMixin, Users):
#     pass