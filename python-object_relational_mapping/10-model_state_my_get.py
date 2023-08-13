#!/usr/bin/python3
""" Script that prints the State object with the name passed as an argument
to the database hbtn_0e_6_usa. Takes 4 arguments: mysql username,
mysql password, database name and name.
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
    State = session.query(State).\
        filter(State.name == sys.argv[4]).first()
    if State:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close
