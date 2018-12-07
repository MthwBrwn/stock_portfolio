from . import app

# 3rd prty requirements
from flask import render_template, redirect, url_for, abort
from sqlalchemy.exc import IntegrityError
from .forms import CompanySearchForm
# API requests
import requests as req
from models import Company, db

import json
import os


# helpers

def get_stock_info(stock):
    return req.get(f"{os.getenv('API_URL')}{code}&APPID={os.getenv('API_KEY')}")


# controllers

@app.route('/')
def home():
    """ this route is the home page for the stocks app """
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])

def company_search():
    """ """
    form = CompanySearchForm

    if form.validate_on_submit():
        res = req.get(f'https://api.iextrading.com/1.0/stock/{ form.data["symbol"] }/company')
        try:
            data = jason.loads(res.text)
            company = {
                'symbol': data['symbol'],
                'companyName': data['companyName'],
                'exchange': data['exchange'],
                'industry': data['industry'],
                'website': data['website'],
                'description': data['description'],
                'CEO': data['CEO'],
                'issueType': data['issueType'],
                'sector': data['sector'],
            }

            new_company = Company(**company)

            db.session.add(new_company)
            db.session.commit()

            return redirect(url_for('.port'))

        except json.JSONDecodeError:
            abort(404)

    return render_template(portfolio/search.htm)


@app.route('/portfolio')
def portfolio_detail():
    """
    """
    return render_template('portfolio/portfolio.html', form = form)
