from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session


from models import db
from models.user import User

import random

auth = Blueprint("auth", __name__)


from models.user import User


def generate_account_number():

    last_user = User.query.order_by(
        User.id.desc()
    ).first()

    if last_user:
        last_number = int(
            last_user.account_number.replace("ACC", "")
        )
        return f"ACC{last_number + 1:06d}"

    return "ACC100001"


@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form["full_name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match"

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:
            return "Email already registered"

        hashed_password = generate_password_hash(password)

        new_user = User(
            full_name=full_name,
            email=email,
            password=hashed_password,
            account_number=generate_account_number()
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.register"))

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:
            return "User not found"

        if not check_password_hash(
            user.password,
            password
        ):
            return "Invalid Password"

        session["user_id"] = user.id

        return redirect("/dashboard")

    return render_template("login.html")

@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")