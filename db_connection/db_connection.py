import psycopg2
import os

# Database Configuration (Modify as needed)
DB_CONFIG = {
    "dbname": "your_db",
    "user": "your_user",
    "password": "your_password",
    "host": "your_host",
    "port": "5432"
}

def connect_db():
    """Establish a PostgreSQL connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def execute_query(sql_query):
    """Execute SQL query and fetch results"""
    conn = connect_db()
    if conn is None:
        return {"error": "Database connection failed"}

    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.commit()
        return results
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
