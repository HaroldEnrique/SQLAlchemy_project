from sqlalchemy import create_engine

#The Engine is how SQLAlchemy communicates with your database
engine = create_engine('sqlite:///test3.db', echo=True) # set True to view logs
engine.execute("PRAGMA journal_mode=WAL")
# First mode to connet to sqlite using sqlalchemy
engine.execute('CREATE TABLE "EX1" (id INTEGER NOT NULL, name VARCHAR, PRIMARY KEY(id));')  #implicity it calls to connect() method
#engine.table_names() # show tables

# Second mode to connect to sqlite using sqlalchemy
conn = engine.connect()
trans = conn.begin()
conn.execute('INSERT INTO "EX1" (name) '
             'VALUES ("Hello")')
trans.commit()

#from configdb import DBSession

