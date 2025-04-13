import jwt
import datetime
import pyodbc

# Define your secret key
SECRET_KEY = "Password123!"

# SQL Server connection string.
# Adjust the DRIVER if necessary.
SQL_CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=WIN-BFCMJ0JFNK5\\SQLEXPRESS;"
    "DATABASE=API;"
    "Trusted_Connection=yes;"
)

# Generate JWT
def generate_jwt():
    """
    Generate a JWT with custom claims.
    - 'user_id' and 'username' are example claims.
    - 'iat' is the issued-at time (UTC).
    - 'exp' is set to one hour from now.
    """
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    payload = {
        "user_id": "12345",
        "username": "exampleuser",
        "iat": now_utc,
        "exp": now_utc + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Update JWT in the SQL Server Database
def update_token_in_db(token):
    """
    Connect to SQL Server and update the JWT in the Token table where ID=1.
    Assumes a table 'Token' with at least a column 'JWT' and a primary key 'ID'.
    """
    try:
        cnxn = pyodbc.connect(SQL_CONNECTION_STRING)
        cursor = cnxn.cursor()
        update_query = "UPDATE Token SET JWT = ? WHERE ID = 1"
        cursor.execute(update_query, token)
        cnxn.commit()
        print("Database update successful. Rows affected:", cursor.rowcount)
    except Exception as e:
        print("Database update failed:", e)
    finally:
        cursor.close()
        cnxn.close()

# Generate JWT and Update Database
if __name__ == "__main__":
    token = generate_jwt()
    print("Generated JWT:")
    print(token)
    update_token_in_db(token)
