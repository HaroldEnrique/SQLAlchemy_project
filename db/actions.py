from db import configdb, model
#import model

User = model.User
session = configdb.DBSession()

def add_user():
    user = model.User(name='John Snow', password='543')
    session.add(user)
    session.commit()

    print(user.id)  # None
