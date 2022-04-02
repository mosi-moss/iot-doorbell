from doorbell import db
from doorbell.models import User
import os

def create_database():
    # create database
    print("Creating database.") 
    db.create_all()
    print("Database created successfully.")
    user = User(
        username = "admin",
        password = "admin"
        )
    db.session.add(user)
    db.session.commit()

# check for, and delete, existing database
if os.path.exists("doorbell/database.db"):
    delete = input("Delete database? Y/n: ")
    if delete.lower() == "y":
        print("Deleting existing database.")
        os.remove("doorbell/database.db")
        create_database()
    else:
        print("No action taken.")
else:
    print("Database does not exist.") 
    create_database()