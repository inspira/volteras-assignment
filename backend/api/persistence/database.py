# -*- coding: utf-8 -*-
"""
Sqlachemy engine and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URL

# See https://fastapi.tiangolo.com/tutorial/sql-databases/ for details

connect_args={}

if SQLALCHEMY_DATABASE_URL.find('sqlite') != -1:
    connect_args["check_same_thread"] = False

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_session():
    """
    Instantiate a new session object
    """
    db_session = SessionLocal()
    return db_session
