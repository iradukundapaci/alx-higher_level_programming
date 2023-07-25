#!/usr/bin/python3
"""
    This scripts prints the first state
    from the database 'hbtn_0e_6_usa'.
"""

if __name__ == "__main__":
    """ Get state the first state
        from the database
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import State, Base

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).all()

    if result is not None:
        for i in result:
            print(i)
    else:
        print("Nothing")

    session.close()
