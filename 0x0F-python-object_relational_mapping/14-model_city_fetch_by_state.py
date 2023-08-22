#!/usr/bin/python3
""" Delete a state containing 'a' from the database"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    """creating a link to db and query"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State).all()
    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")
session.close()
