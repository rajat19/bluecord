import psycopg2
from datetime import datetime
import settings as my_settings


def create_db_connection():
    config = {
        'user': my_settings.DB_USER,
        'password': my_settings.DB_PASSWORD,
        'host': my_settings.DB_HOST,
        'database': my_settings.DB_NAME,
        'sslmode': 'allow'
    }
    # conn = psycopg2.connect(**config)
    conn = psycopg2.connect(my_settings.DATABASE_URL)
    return conn


def post_search_data(user_id, keyword):
    connection = create_db_connection()
    sql_cursor = connection.cursor()
    sql_cursor.execute("Insert into searches Values('{}', '{}', '{}')".format(
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