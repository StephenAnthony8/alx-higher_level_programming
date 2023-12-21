#!/usr/bin/python3
"""model_state_fetch_all script"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from model_state import State, Base
import sys


def query_state():
    host = 'localhost'
    port = '3306'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db_url = f'mysql+mysqldb://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")


def main():
    query_state()


if __name__ == "__main__":
    main()
