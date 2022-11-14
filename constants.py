import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

OXFORD_ID = os.getenv("OXFORD_ID")
OXFORD_SECRET = os.getenv("OXFORD_SECRET")

DB_HOST = os.getenv('DB_HOST') or 'localhost'
DB_NAME = os.getenv('DB_NAME') or 'verbos'
DB_USER = os.getenv('DB_USER') or 'postgres'
DB_PASSWORD = os.getenv('DB_PASSWORD') or ''

