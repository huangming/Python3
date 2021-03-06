# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, String, Integer

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

from sqlalchemy import inspect

db_uri = 'sqlite:///db.db'
#db_uri = 'sqlite:///db.sqlite'
engine = create_engine(db_uri)
session.query(User).filter_by(name='ed').all()

# query with multiple classes, returns tuples
session.query(User, Address).join('addresses').filter_by(name='ed').all()

# query using orm-enabled descriptors
session.query(User.name, User.fullname).all()

# query from a mapper
user_mapper = class_mapper(User)
session.query(user_mapper)