from flask import Flask, request, redirect, url_for, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="atown",
    password="Not giving you the password here, lol",
    hostname="atown.mysql.pythonanywhere-services.com",
    databasename="atown$heartrates",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class HeartRates(db.Model):
    __tablename__ = "heartrates"
    id = db.Column(db.Integer, primary_key=True)
    heartrate = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(4096), nullable=False)

@app.route('/')
def main():
    return redirect(url_for('get_all_heartrates'))

@app.route('/add_heartrate', methods=["POST"])
def add_heartrate():
    try:
        heartrate_value = int(request.form["heartrate"])  # Ensure it's an integer
        info = HeartRates(heartrate=heartrate_value, date=str(datetime.now()))
        db.session.add(info)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return redirect(url_for('get_all_heartrates'))

@app.route('/get_all_heartrates', methods=["GET"])
def get_all_heartrates():
    return render_template("all_heartrates.html", info=HeartRates.query.all())

@app.route('/get_latest_heartrate', methods=["GET"])
def get_latest_heartrate():
    latest_hr = HeartRates.query.order_by(HeartRates.id.desc()).first()
    if latest_hr:
        return jsonify({
            "info": "This is the most recent heartrate found",
            "heartrate": latest_hr.heartrate,
            "date": latest_hr.date
        })
    else:
        return jsonify({"message": "No heart rate records found"}), 404


if __name__ == "__main__":
    #run on an unused port
    app.run(port=4237)
