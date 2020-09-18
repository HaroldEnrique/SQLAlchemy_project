from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.engine import Engine
from sqlalchemy import event

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from db import varsdb, model
#import varsdb, actions, model

engine = create_engine('sqlite:///'+varsdb.db_path, echo=True) # set False in production mode
engine.execute("PRAGMA journal_mode="+varsdb.journal_mode)

#dbapi_conn = engine.raw_connection()

#@event.listens_for(Engine, "connect")
#def set_sqlite_pragma(dbapi_connection, connection_record):
#    print("New DBAPI connection:", dbapi_connection)
#    print("Connection record:", connection_record)
#    print("here is event listener connect")
#    cursor = dbapi_connection.cursor()
#    cursor.execute("PRAGMA journal_mode=WAL")
#    cursor.close()
#

#DBSession = scoped_session(sessionmaker(bind=engine))
DBSession = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

#session = DBSession()
#actions
#actions.add_user(session)
#print()
#model.User.find_by_name(session, 'John ERE')