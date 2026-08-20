from flask import Flask, render_template, session, redirect
import config

from models import db
from models.user import User
from models.transaction import Transaction

from routes.auth import auth
from routes.customer import customer


app = Flask(__name__)


# --------------------------------------------------
# Flask Configuration
# --------------------------------------------------

app.config["SECRET_KEY"] = config.SECRET_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = (
    config.SQLALCHEMY_DATABASE_URI
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = (
    config.SQLALCHEMY_TRACK_MODIFICATIONS
)


# --------------------------------------------------
# Initialize Database
# --------------------------------------------------

db.init_app(app)


# --------------------------------------------------
# Register Blueprints
# --------------------------------------------------

app.register_blueprint(auth)
app.register_blueprint(customer)


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# --------------------------------------------------
# Customer Dashboard
# --------------------------------------------------

@app.route("/dashboard")
def dashboard():

    # Check whether user is logged in

    if "user_id" not in session:
        return redirect("/login")


    # Get logged-in user

    user = db.session.get(
        User,
        session["user_id"]
    )


    # User no longer exists

    if not user:

        session.clear()

        return redirect("/login")


    return render_template(
        "dashboard.html",
        user=user
    )


# --------------------------------------------------
# Create Database Tables
# --------------------------------------------------

with app.app_context():

    db.create_all()


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)