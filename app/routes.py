from . import app

# 3rd prty requirements
from flask import render_template, abort, redirect, url_for, session, g, make_response
from sqlalchemy.exc import IntegrityError

# API requests
import requests as req
from json import JSONDecodeError
import json
import os


# helpers

def get_stock_info(code):
    return req.get(f"{os.getenv('API_URL')}{code}&APPID={os.getenv('API_KEY')}")


# controllers

@app.route('/')
def home()
    """ this route is the home page for the stocks app """
    return 'test'
