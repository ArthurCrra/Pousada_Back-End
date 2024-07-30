import psycopg2
from psycopg2 import OperationalError
import os

os.environ['DB_HOST'] = 'localhost'
os.environ['DB_NAME'] = 'postgres'
os.environ['DB_USER'] = 'postgres'
os.environ['DB_PASSWORD'] = '12345'
os.environ['DB_PORT'] = '5432'

def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT', '5432')  # Valor padrão para a porta
        )
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return conn

