#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name="California")
    newCity = City(name="San Francisco", state=newState)
    session.add(newCity)
    session.commit()

    session.close()
