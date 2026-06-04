from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registrant(db.Model):
    __tablename__ = 'registrants'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    sport = db.Column(db.String, nullable=False)

def connect_to_db(flask_app):
    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()

    print("Connected to the db!")

if __name__ == '__main__':
    from app import app
    connect_to_db(app)
    