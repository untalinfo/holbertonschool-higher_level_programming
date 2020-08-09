#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from relationship_state import State
from relationship_city import Base, City
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

    sql_query = session.query(State).order_by(State.id)
    for state in sql_query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
