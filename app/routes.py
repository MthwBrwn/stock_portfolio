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

def get_stock_info(stock):
    return req.get(f"{os.getenv('API_URL')}{code}&APPID={os.getenv('API_KEY')}")


# controllers

@app.route('/')
def home():
    """ this route is the home page for the stocks app """
    return 'test'

def stock_search():
    """This retrieves the stock info from the API"""
    form = StockSearchForm()
    if form.validate_on_submit():
        stock = form.data['stock_name']
        res = get_stock_info(stock)

        try:
            session['context'] = res.text
            return redirect(url_for('.stock_detail')
        except JSONDecodeError:
            abort(404)
    return render_template(search.html, form=form)

@app.route('/stocks')
@app.route('/stocks/<stock_name>')

def stock_detail(stock_name = None):

    if stock_name:
        res = get_stock_info(code)
        return render_template('stock_detail.html', **res.json())

    else:

        try:
            context=json.loads(session['context'])
            stock=StockModel(stockName=context['name'])
            print('stock', stock)
            db.session.add(stock)
            db.session.commit()
            return render_template('stock_detail.html', **context)
        except IntegrityError as e:
            print(e)
            res=make_response('That stock already added :(', 400)
            return res
