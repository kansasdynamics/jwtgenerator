# JWT Generator and Database Updater

This project contains a Python script that generates a JSON Web Token (JWT) using PyJWT and then updates a record in a SQL Server database using pyodbc. It provides a simple, OAuth-free method for obtaining an API authorization token.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Script Overview](#script-overview)
- [License](#license)

## Prerequisites

- **Python 3.x** (Download from [python.org/downloads](https://www.python.org/downloads/))
- **SQL Server** with the necessary access (e.g., SQLEXPRESS)
- **ODBC Driver for SQL Server** (e.g., ODBC Driver 17 for SQL Server or ODBC Driver 18)

## Installation

Follow these commands in your terminal to set up your Python environment:

1. Upgrade pip:
    ```bash
    python -m pip install --upgrade pip
    ```

2. Install required Python packages:
    ```bash
    pip install PyJWT
    pip install pyodbc
    ```

## Configuration

Before running the script, you may need to modify a few configuration settings in `Generate_JWT.py` for your environment:

### Secret Key

Replace the secret key with your own secure value:
```python
SECRET_KEY = "Password123!"  # Replace with your secure secret key.
```

## Additional Notes

- **Environment Changes:**  
  In a new environment, remember to update the following:
  - The `SECRET_KEY` to your new secure value.
  - The `SQL_CONNECTION_STRING` to match your new SQL Server instance and database.
  - The database update query if your table structure is different.
- **Running the Script:**  
  Run `python Generate_JWT.py` after making these changes.
