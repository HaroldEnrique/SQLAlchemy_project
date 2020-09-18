from db import actions, model, configdb


if __name__ == "__main__":
    
    #engine, session = start()
    #add_user()
    #actions.add_user()
    session = configdb.DBSession()
    john = model.User.find_by_name(session, 'John Snow')
    print(john)