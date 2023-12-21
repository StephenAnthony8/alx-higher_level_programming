#!/usr/bin/python3
"""model-state script"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State object"""
    __tablename__ = "states"
    id = Column('id', Integer, primary_key=True)
    name = Column("name", String(50))


if __name__ == "__main__":
    host = 'localhost'
    port = '3306'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db_url = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
