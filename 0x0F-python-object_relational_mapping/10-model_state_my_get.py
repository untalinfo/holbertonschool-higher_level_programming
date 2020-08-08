#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]
    state = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dataBase),
                           pool_pre_ping=True)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    sql_query = session.query(State).filter(State.name == state).first()
    if sql_query is None:
        print("Not found")
    else:
        print(sql_query.id)
    session.close()
