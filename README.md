# 🏦 SecureBank — Banking Management System

A full-stack **Banking Management System** built using **Python, Flask, MySQL, SQLAlchemy, HTML, CSS, and Jinja2**.

The application provides a simulated banking environment where customers can create accounts, securely log in, view their account balance, deposit money, withdraw money, and track their complete transaction history.

This project was developed to demonstrate practical skills in **Python backend development, Flask, relational database management, authentication, session handling, SQLAlchemy ORM, CRUD operations, transaction processing, and frontend web development**.

> ⚠️ **Note:** This is an educational banking simulation and is not intended for processing real financial transactions.

---

# 📌 Project Overview

The **SecureBank Banking Management System** is a web-based banking application designed to simulate the basic operations performed by a customer in a banking environment.

The system allows a registered customer to:

* Create a bank account
* Log in using their credentials
* Access a personalized dashboard
* View their current account balance
* Deposit money
* Withdraw money
* View transaction history
* Log out securely

The application uses **Flask** as the backend web framework and **MySQL** as the relational database.

**SQLAlchemy** is used as the ORM layer to communicate with the MySQL database.

---

# ✨ Key Features

## 👤 1. Customer Registration

New customers can register themselves through the registration page.

The registration process collects the required customer information and creates a new record in the MySQL database.

### Registration functionality includes:

* Customer name
* Email / username
* Password
* Account creation
* Input validation
* Duplicate account checking

After successful registration, the customer can log in to their account.

---

# 🔐 2. Customer Login

Registered customers can log in through the login page.

The system verifies the provided credentials before allowing access to the banking dashboard.

After successful authentication, a Flask session is created to identify the logged-in customer.

Unauthorized users cannot directly access protected banking pages.

---

# 📊 3. Customer Dashboard

The dashboard is the main page available after login.

It provides an overview of the customer's banking account.

The dashboard can display:

* Customer information
* Current account balance
* Deposit option
* Withdrawal option
* Transaction history
* Logout option

The dashboard is designed to provide quick access to the major banking operations.

---

# 💰 4. Deposit Money

Customers can deposit money into their accounts.

The deposit process follows this workflow:

```text
Customer enters amount
        ↓
Validate amount
        ↓
Check amount is valid
        ↓
Update customer balance
        ↓
Create transaction record
        ↓
Save changes to MySQL
        ↓
Display updated balance
```

### Example

If the customer's current balance is:

```text
₹10,000
```

and they deposit:

```text
₹5,000
```

the new balance becomes:

```text
₹15,000
```

A corresponding deposit transaction is also stored in the transaction table.

---

# 💸 5. Withdraw Money

Customers can withdraw money from their account.

Before processing a withdrawal, the system checks whether the customer has sufficient funds.

### Withdrawal workflow

```text
Customer enters withdrawal amount
              ↓
       Validate amount
              ↓
     Check current balance
              ↓
       ┌──────┴──────┐
       ↓             ↓
 Sufficient      Insufficient
   balance          balance
       ↓             ↓
 Process          Reject
 withdrawal      withdrawal
       ↓
 Update balance
       ↓
 Create transaction
       ↓
 Save to MySQL
```

### Example

Current balance:

```text
₹20,000
```

Withdrawal:

```text
₹7,000
```

Remaining balance:

```text
₹13,000
```

If a customer attempts to withdraw more than their available balance, the system rejects the transaction.

---

# 📜 6. Transaction History

Every successful banking operation is recorded in the database.

Customers can access their transaction history through the transactions page.

Transaction information can include:

* Transaction ID
* Transaction type
* Transaction amount
* Transaction date/time
* Customer associated with the transaction

Example:

| Type       |  Amount | Description     |
| ---------- | ------: | --------------- |
| Deposit    |  ₹5,000 | Money deposited |
| Withdrawal |  ₹2,000 | Money withdrawn |
| Deposit    | ₹10,000 | Money deposited |

This allows customers to track their banking activity.

---

# 🚪 7. Logout

Customers can log out of their account using the logout functionality.

The Flask session is cleared so that the authenticated account is no longer accessible through the current session.

---

# 🛠️ Technology Stack

## Backend

* **Python**
* **Flask**
* **SQLAlchemy**
* **Flask-SQLAlchemy**

## Frontend

* **HTML5**
* **CSS3**
* **Jinja2 Templates**

## Database

* **MySQL**

## Version Control

* **Git**
* **GitHub**

## Development Environment

* Linux / Ubuntu
* VS Code
* Python Virtual Environment

---

# 🏗️ Application Architecture

The project follows a modular Flask application structure.

```text
BankingSystem/
│
├── app.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── transaction.py
│
├── routes/
│   └── customer.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── deposit.html
│   ├── withdraw.html
│   └── transactions.html
│
├── static/
│   └── css/
│       └── style.css
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

> The exact directory structure may vary slightly depending on the current version of the project.

---

# 🧩 Project Components

## `app.py`

The main Flask application entry point.

It is responsible for:

* Creating the Flask application
* Configuring the application
* Connecting SQLAlchemy
* Registering blueprints/routes
* Starting the development server

---

# 👤 User Model

The User model represents customers of the banking system.

It is responsible for storing customer-related information in MySQL.

A typical user record contains information such as:

```text
User
├── ID
├── Name
├── Email
├── Password
├── Balance
└── Account information
```

The User model is used whenever the application needs to:

* Create a customer
* Authenticate a customer
* Retrieve account information
* Update account balance

---

# 💳 Transaction Model

The Transaction model stores banking operations performed by customers.

A transaction is associated with a specific customer.

Conceptually:

```text
User
 │
 │
 │ 1
 │
 │
 │ N
 ▼
Transaction
```

This represents a **one-to-many relationship**:

> One customer can have many transactions.

---

# 🗄️ MySQL Database

The project uses **MySQL** as its relational database.

The database stores:

* Customer accounts
* Customer credentials
* Account balances
* Transaction records

Using MySQL makes the application suitable for learning how real-world web applications interact with relational databases.

---

# 🔗 Database Relationship

The major relationship in the application is:

```text
             ┌─────────────────────┐
             │        USER         │
             ├─────────────────────┤
             │ id                  │
             │ name                │
             │ email               │
             │ password            │
             │ balance             │
             └──────────┬──────────┘
                        │
                        │ 1
                        │
                        │ N
                        ▼
             ┌─────────────────────┐
             │    TRANSACTION     │
             ├─────────────────────┤
             │ id                  │
             │ user_id             │
             │ type                │
             │ amount              │
             │ created_at          │
             └─────────────────────┘
```

The `user_id` in the transaction table associates each transaction with its corresponding customer.

---

# 🔄 Complete Application Flow

The overall application flow is:

```text
                    START
                      │
                      ▼
              ┌───────────────┐
              │  Registration │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │     Login     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   Dashboard   │
              └───────┬───────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
      Deposit      Withdraw   Transactions
          │           │           │
          │           │           │
          ▼           ▼           │
       Update      Update         │
       Balance     Balance        │
          │           │           │
          └──────┬────┘           │
                 │                │
                 ▼                │
          Create Transaction ◄────┘
                 │
                 ▼
              MySQL
```

---

# 💻 Main Routes

The application contains routes for the major banking operations.

Typical routes include:

| Route           | Method     | Purpose                 |
| --------------- | ---------- | ----------------------- |
| `/register`     | GET / POST | Customer registration   |
| `/login`        | GET / POST | Customer authentication |
| `/dashboard`    | GET        | Customer dashboard      |
| `/deposit`      | GET / POST | Deposit money           |
| `/withdraw`     | GET / POST | Withdraw money          |
| `/transactions` | GET        | Transaction history     |
| `/logout`       | GET        | Logout customer         |

The exact routes may vary depending on the current implementation.

---

# 🔒 Authentication & Security

The application implements basic authentication and access control.

Security-related functionality includes:

### Session Management

Flask sessions are used to maintain the logged-in customer's state.

### Protected Pages

Banking pages such as:

* Dashboard
* Deposit
* Withdrawal
* Transactions

should only be accessible to authenticated customers.

### Balance Validation

Withdrawals are checked against the customer's available balance.

### Input Validation

The application validates transaction amounts before modifying the account.

### Database Operations

SQLAlchemy is used to interact with MySQL instead of manually constructing SQL queries throughout the application.

> For a production banking application, additional security measures such as password hashing, CSRF protection, HTTPS, rate limiting, multi-factor authentication, audit logging, and stronger authorization controls would be required.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/toufikumarsekh/banking-system.git
```

Move into the project:

```bash
cd banking-system
```

---

# 🐍 2. Create a Virtual Environment

On Linux/macOS:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

# 📦 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🗄️ 4. Configure MySQL

Make sure MySQL is installed and running.

Create a database for the project.

For example:

```sql
CREATE DATABASE banking_system;
```

Then configure the application's MySQL connection according to the configuration used in the project.

A typical SQLAlchemy MySQL connection looks like:

```text
mysql+pymysql://USERNAME:PASSWORD@localhost/banking_system
```

Replace:

```text
USERNAME
PASSWORD
```

with your local MySQL credentials.

---

# 🔑 5. Configure Environment Variables

If the project uses a `.env` file, create one in the project root.

Example:

```env
SECRET_KEY=your-secret-key

DATABASE_URL=mysql+pymysql://username:password@localhost/banking_system
```

> Never upload your `.env` file or real database credentials to GitHub.

Add it to `.gitignore`:

```gitignore
.env
```

---

# ▶️ 6. Run the Application

Start the Flask application:

```bash
python app.py
```

The application should start on:

```text
http://127.0.0.1:5000
```

Open the address in your browser.

---

# 🧪 Testing the Application

After starting the application, test the following workflow.

## Test 1 — Create Account

1. Open the registration page.
2. Enter customer details.
3. Submit the registration form.
4. Verify that the account is created.

---

## Test 2 — Login

1. Open the login page.
2. Enter the registered credentials.
3. Submit the form.
4. Verify that the dashboard opens.

---

## Test 3 — Check Balance

After login:

1. Open the dashboard.
2. Check the displayed account balance.
3. Verify that the balance matches the database.

---

## Test 4 — Deposit

1. Open Deposit.
2. Enter a valid amount.
3. Submit.
4. Verify the balance increases.
5. Open Transactions.
6. Verify that a deposit transaction was created.

---

## Test 5 — Withdrawal

1. Open Withdrawal.
2. Enter an amount lower than the current balance.
3. Submit.
4. Verify that the balance decreases.
5. Check the transaction history.

---

## Test 6 — Insufficient Balance

Try withdrawing more money than the current account balance.

The application should reject the transaction and prevent the account from going into an invalid negative balance.

---

# 📸 Screenshots

You can add screenshots of the application here to make the GitHub repository more attractive.

Recommended screenshots:

```text
screenshots/
│
├── home.png
├── register.png
├── login.png
├── dashboard.png
├── deposit.png
├── withdraw.png
└── transactions.png
```

Example:

```markdown
![Customer Dashboard](screenshots/dashboard.png)
```

Recommended screenshots for the GitHub repository:

* 🏠 Home page
* 📝 Registration page
* 🔐 Login page
* 📊 Dashboard
* 💰 Deposit page
* 💸 Withdrawal page
* 📜 Transaction history

---

# 🚀 Future Enhancements

The current system implements the core banking workflow, but it can be expanded significantly.

## 🔐 Advanced Authentication

Future versions could include:

* Secure password hashing
* Email verification
* Password reset
* OTP authentication
* Two-factor authentication
* Account lockout after repeated failed logins

---

## 💸 Money Transfer

A transfer system could allow one customer to send money to another customer.

Example:

```text
Customer A
₹20,000
   │
   │ Transfer ₹5,000
   ▼
Customer B
₹10,000
```

After the transaction:

```text
Customer A → ₹15,000
Customer B → ₹15,000
```

Both sides could receive transaction records.

---

## 💳 Account Numbers

The system could generate unique bank account numbers for customers.

Example:

```text
Account Number: 100245789631
```

This could then be used for:

* Transfers
* Deposits
* Withdrawals
* Account identification

---

## 👨‍💼 Admin Dashboard

An administrative interface could be added.

Admins could:

* View all customers
* View all transactions
* Search customers
* Search transactions
* Disable accounts
* Monitor suspicious activity
* Generate reports

---

## 📊 Banking Analytics

The dashboard could include visual statistics such as:

* Monthly deposits
* Monthly withdrawals
* Total transactions
* Spending patterns
* Account activity

Charts could be implemented using JavaScript charting libraries.

---

## 📄 Bank Statement

Users could download their transaction history as:

* PDF
* CSV
* Excel

---

## 📱 Responsive Design

The application can be further optimized for:

* Desktop
* Tablet
* Mobile

---

## 🌐 Production Deployment

The application can eventually be deployed using:

* Render
* Railway
* AWS
* Google Cloud
* Azure

For production use, the application should use:

* PostgreSQL/MySQL
* HTTPS
* Environment variables
* Production WSGI server
* Secure secret management
* Proper database migrations
* Logging and monitoring

---

# 📚 Learning Objectives

This project helped demonstrate practical understanding of:

### Python

* Functions
* Classes
* Modules
* Exception handling
* Database interaction

### Flask

* Application setup
* Routing
* Blueprints
* Request handling
* Sessions
* Redirects
* Templates
* Jinja2

### Database

* MySQL
* Relational database design
* Tables
* Primary keys
* Foreign keys
* Relationships
* SQLAlchemy ORM
* CRUD operations

### Frontend

* HTML5
* CSS3
* Forms
* Jinja templates
* Responsive UI

### Software Development

* Project structure
* Virtual environments
* Dependency management
* Git
* GitHub
* Debugging

---

# 🔧 Git & GitHub

This project is maintained using Git.

To get the latest version:

```bash
git pull
```

After making changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Update banking system"
```

Push the changes:

```bash
git push
```

---

# 📁 Important Files

| File / Folder      | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| `app.py`           | Main Flask application                                    |
| `models/`          | Database models                                           |
| `user.py`          | Customer/user model                                       |
| `transaction.py`   | Transaction model                                         |
| `templates/`       | HTML/Jinja pages                                          |
| `static/`          | CSS and frontend assets                                   |
| `requirements.txt` | Python dependencies                                       |
| `.gitignore`       | Prevents sensitive/unnecessary files from being committed |
| `README.md`        | Project documentation                                     |

---

# ⚠️ Security Disclaimer

This application is intended for **educational and portfolio purposes**.

It is **not a production banking system**.

Do not use:

* Real banking credentials
* Real account numbers
* Real financial information
* Real payment credentials
* Production customer data

A real banking platform requires extensive security, compliance, auditing, encryption, fraud detection, access control, and regulatory requirements.

---

# 👨‍💻 Author

## Toufik Umar Sekh

Computer Science & Engineering

### GitHub

https://github.com/toufikumarsekh

### Project Repository

https://github.com/toufikumarsekh/banking-system

---

# ⭐ Project Highlights

This project demonstrates a complete backend-driven web application with:

```text
Python
   +
Flask
   +
SQLAlchemy
   +
MySQL
   +
HTML/CSS
   +
Jinja2
   +
Authentication
   +
Database Management
   +
Banking Transactions
```

The project can serve as a foundation for developing a more advanced financial management platform.

---

# 📜 License

This project is intended primarily for educational and portfolio purposes.

You are free to study, modify, and extend the project for learning and development.
