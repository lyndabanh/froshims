from flask import Flask, render_template, request, redirect, jsonify, flash
from config import Config
from model import connect_to_db
from crud import register_for_sport, deregister_for_sport, all_registrants

app = Flask(__name__)
app.secret_key = "dev"
app.config.from_object(Config)

# REGISTRANTS = {}
SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")
    
    # Remember registrant
    success = register_for_sport(name, sport)
    if success:
        # return jsonify({'message': 'Registration successful'}), 200
        flash("You're registered!")
        return redirect("/registrants")
    else:
        return jsonify({
            'error': 'Name already exists',
            'message': 'Please choose a different name'         
        }), 409

@app.route("/registrants")
def registrants():
    registrants = all_registrants()
    return render_template("registrants.html", registrants=registrants)

@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if not id:
        return render_template("failure.html")
    
    success = deregister_for_sport(id)
    if success:
        flash("You've deregistered!")
        return redirect("/registrants")
    else:
        return jsonify({
            'error': 'Deregistration unsuccessful',
            'message': 'Please try again'
        }), 409
    return render_template("deregister.html", id=id)

if __name__ == '__main__':
    connect_to_db(app)
    app.run()
