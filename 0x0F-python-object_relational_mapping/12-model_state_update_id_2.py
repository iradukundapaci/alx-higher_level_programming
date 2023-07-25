#!/usr/bin/python3
""" Sripts that updates a state in States
    table
"""

if __name__ == "__main__":
    """Sripts imports State class for the
       objects
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.id == 2)
    result.update({State.name: 'New Mexico'})
    session.commit()

    session.close()
