class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///froshims.db'
    # Flask-SQLAlchemy will log all database activity to Python's stderr for debugging purposes
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFCATIONS = False
