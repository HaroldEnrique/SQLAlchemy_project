from sqlalchemy import create_engine

engine = create_engine('sqlite:///test1.db', echo=True) # set False in production mode
engine.execute("PRAGMA journal_mode=WAL")

#dbapi_conn = engine.raw_connection()
#cursor = dbapi_conn.cursor()
#cursor.execute("PRAGMA journal_mode=WAL")
#cursor.close()

