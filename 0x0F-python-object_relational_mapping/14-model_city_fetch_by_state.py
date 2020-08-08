#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dataBase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dataBase),
                           pool_pre_ping=True)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    sql_query = session.query(State, City)\
        .filter(State.id == City.state_id).all()
    for states, cities in sql_query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
