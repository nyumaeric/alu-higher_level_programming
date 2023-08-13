#!/usr/bin/python3
""" Script that prints the first State object from the database hbtn_0e_6_usa.
Takes 3 arguments: mysql username, mysql password and database name.
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if (state is None):
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close
