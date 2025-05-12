import os

# # Get absolute path to the database
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DB_PATH = os.path.join(BASE_DIR, '../../froshims.db')

# class Config:
#     DATABASE = DB_PATH  

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///froshims.db'
    # Flask-SQLAlchemy will log all database activity to Python's stderr for debugging purposes
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFCATIONS = False
