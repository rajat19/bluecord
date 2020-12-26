import os

from dotenv import load_dotenv

load_dotenv()

# CREDENTIALS
BOT_AUTH_TOKEN = os.getenv('BOT_AUTH_TOKEN')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
GOOGLE_API_KEY = os.getenv('GOOGLE_SEARCH_API_KEY')
GOOGLE_CSE_KEY = os.getenv('GOOGLE_CSE_ID')
DATABASE_URL=os.environ['DATABASE_URL']