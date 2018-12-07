from . import app

# 3rd prty requirements
from flask import render_template, redirect, url_for, abort
# from sqlalchemy.exc import IntegrityError
from .forms import CompanySearchForm
# API requests
import requests as req
from .models import Company, db

import json
# import os

# controllers

@app.route('/')
def home():
    """ this route is the home page for the stocks app """
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def company_search():
    """ this is the route for the search page It first validated and
    then attempts to get info form the API """
    form = CompanySearchForm
    if form.validate_on_submit():
        res = req.get(f'https://api.iextrading.com/1.0/stock/{ form.data["symbol"] }/company')
        try:
            data = json.loads(res.text)
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

    return render_template('portfolio/search.html', form=form)


@app.route('/portfolio')
def portfolio_detail():
    """This is the controller for the portfolio page
    """
    return render_template('portfolio/portfolio.html')
