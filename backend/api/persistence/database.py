# -*- coding: utf-8 -*-
"""
Sqlachemy engine and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Returns a new db session
    """
    create_all()
    return SessionLocal()


def create_all():
    """
    Creates the database schema if it is not initialized
    """
    Base.metadata.create_all(bind=engine)
