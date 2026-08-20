from urllib.parse import quote_plus

DB_USER = "bankuser"
DB_PASSWORD = quote_plus("Bank@123")
DB_HOST = "localhost"
DB_NAME = "banking_system"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "banking-system-secret-key"