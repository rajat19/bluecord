import psycopg2
from datetime import datetime
import settings as my_settings


def create_db_connection():
    conn = psycopg2.connect(my_settings.DATABASE_URL)
    return conn

def create_table():
    connection = create_db_connection()
    command = "CREATE TABLE searches (id SERIAL PRIMARY KEY,user_id VARCHAR(255) NOT NULL, keyword VARCHAR(255) NOT NULL, created_at timestamp)"
    sql_cursor = connection.cursor()
    sql_cursor.execute(command)
    connection.commit()
    connection.close()


def post_search_data(user_id, keyword):
    connection = create_db_connection()
    sql_cursor = connection.cursor()
    sql_cursor.execute("Insert into searches (user_id, keyword, created_at) Values('{}', '{}', '{}')".format(
        user_id, keyword, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def fetch_search_data(user_id, keyword):
    connection = create_db_connection()
    sql_cursor = connection.cursor()
    sql_cursor.execute(
        "Select * from searches where user_id = '{}' and keyword like '%".format(user_id) + keyword + "%'")
    results = sql_cursor.fetchall()
    connection.close()
    return results