from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from decimal import Decimal

from models import db
from models.user import User
from models.transaction import Transaction


customer = Blueprint(
    "customer",
    __name__
)


# ==================================================
# DEPOSIT
# ==================================================

@customer.route(
    "/deposit",
    methods=["GET", "POST"]
)
def deposit():

    # Check login

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


    # Handle deposit

    if request.method == "POST":

        amount_text = request.form.get(
            "amount",
            ""
        ).strip()


        # Validate amount

        try:

            amount = Decimal(amount_text)

        except Exception:

            return "Invalid amount"


        # Amount must be positive

        if amount <= 0:

            return "Amount must be greater than zero"


        # Current balance

        current_balance = (
            user.balance or Decimal("0.00")
        )


        # New balance

        new_balance = (
            current_balance + amount
        )


        # Update balance

        user.balance = new_balance


        # Create transaction

        transaction = Transaction(

            user_id=user.id,

            transaction_type="DEPOSIT",

            amount=amount,

            balance_after=new_balance

        )


        # Save transaction

        db.session.add(transaction)

        db.session.commit()


        # Return to dashboard

        return redirect("/dashboard")


    return render_template(
        "deposit.html",
        user=user
    )


# ==================================================
# WITHDRAW
# ==================================================

@customer.route(
    "/withdraw",
    methods=["GET", "POST"]
)
def withdraw():

    # Check login

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


    # Handle withdrawal

    if request.method == "POST":

        amount_text = request.form.get(
            "amount",
            ""
        ).strip()


        # ==========================================
        # VALIDATE AMOUNT
        # ==========================================

        try:

            amount = Decimal(amount_text)

        except Exception:

            return render_template(
                "withdraw.html",
                user=user,
                error="Please enter a valid amount."
            )


        # Amount must be positive

        if amount <= 0:

            return render_template(
                "withdraw.html",
                user=user,
                error="Amount must be greater than zero."
            )


        # ==========================================
        # CURRENT BALANCE
        # ==========================================

        current_balance = (
            user.balance or Decimal("0.00")
        )


        # ==========================================
        # INSUFFICIENT BALANCE CHECK
        # ==========================================

        if amount > current_balance:

            return render_template(
                "withdraw.html",
                user=user,
                error="Insufficient balance."
            )


        # ==========================================
        # NEW BALANCE
        # ==========================================

        new_balance = (
            current_balance - amount
        )


        # Update user balance

        user.balance = new_balance


        # ==========================================
        # CREATE TRANSACTION
        # ==========================================

        transaction = Transaction(

            user_id=user.id,

            transaction_type="WITHDRAW",

            amount=amount,

            balance_after=new_balance

        )


        # Save transaction

        db.session.add(transaction)

        db.session.commit()


        # Return to dashboard

        return redirect("/dashboard")


    return render_template(
        "withdraw.html",
        user=user
    )


# ==================================================
# TRANSACTION HISTORY
# ==================================================

@customer.route("/transactions")
def transactions():

    # ==============================================
    # CHECK LOGIN
    # ==============================================

    if "user_id" not in session:

        return redirect("/login")


    # ==============================================
    # GET LOGGED-IN USER
    # ==============================================

    user = db.session.get(
        User,
        session["user_id"]
    )


    # User no longer exists

    if not user:

        session.clear()

        return redirect("/login")


    # ==============================================
    # GET USER TRANSACTIONS
    # ==============================================

    transactions = Transaction.query.filter_by(

        user_id=user.id

    ).order_by(

        Transaction.created_at.desc()

    ).all()


    # ==============================================
    # CALCULATE TOTAL DEPOSITS
    # ==============================================

    total_deposits = sum(

        (
            transaction.amount

            for transaction in transactions

            if transaction.transaction_type == "DEPOSIT"
        ),

        Decimal("0.00")

    )


    # ==============================================
    # CALCULATE TOTAL WITHDRAWALS
    # ==============================================

    total_withdrawals = sum(

        (
            transaction.amount

            for transaction in transactions

            if transaction.transaction_type == "WITHDRAW"
        ),

        Decimal("0.00")

    )


    # ==============================================
    # TOTAL TRANSACTION COUNT
    # ==============================================

    transaction_count = len(
        transactions
    )


    # ==============================================
    # SHOW TRANSACTION PAGE
    # ==============================================

    return render_template(

        "transactions.html",

        user=user,

        transactions=transactions,

        total_deposits=total_deposits,

        total_withdrawals=total_withdrawals,

        transaction_count=transaction_count

    )