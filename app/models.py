from . import app

# data base Imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime as dt


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models

class Company(db.Model):
    __tablename__= 'companies'

    id = db.Column(db.Integer, primary_key=True)
    symbol =Column(db.String(64), index=True, unique=True)
    # come back and finish!!!
    C


# `flask db init` - Creates migrations directory and configs  (ONLY RUN ONCE)
# `flask db migrate -m 'migration message'` - creates migrations and preps DB
# `flask db upgrade` - creates tables
    # StocksModel(db.Model):
    # __tablename__ = 'stocks'

    # id = db.Column(db.Integer, primary_key=True)
    # stockName = db.Column(db.String(256), index=True, unique=True)
    # date_created = db.Column(db.DateTime, default=dt.now())

    # def __repr__(self):
    #     return '<Stock {}>'.format(self.stockName)
