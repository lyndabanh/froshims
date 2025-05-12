from model import db, Registrant
from sqlalchemy.exc import IntegrityError

def register_for_sport(name, sport):
    registrant = Registrant(name=name, sport=sport)

    try:
        db.session.add(registrant)
        db.session.commit()
        return True
    except IntegrityError as e:
        db.session.rollback()
        print(f"IntegrityError occurred: {e}")
        return False
    
def deregister_for_sport(id):
    registrant = Registrant.query.get(id)
    if registrant is None:
        return False

    db.session.delete(registrant)
    db.session.commit()
    return True

def all_registrants():
    # with db.session.begin():
    #     registrants = db.session.execute(
    #         text("SELECT * FROM registrants")
    #     ).fetchall()
    # return registrants
    return Registrant.query.all()
