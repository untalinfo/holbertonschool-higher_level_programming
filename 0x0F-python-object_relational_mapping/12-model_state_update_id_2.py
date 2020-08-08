#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

from model_state import Base, State
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

    rename = session.query(State).filter(State.id == 2).first()
    rename.name = 'New Mexico'
    session.commit()
    session.close()
