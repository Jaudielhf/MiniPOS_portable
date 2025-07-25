import sqlite3
from sqlite3 import Connection, Cursor
import os
from typing import Optional
from sqlite3 import Connection

class DBManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn: Optional[Connection] = None

    def connect(self):
   # Asegurar que el directorio existe antes de conectar
        dir_path = os.path.dirname(self.db_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        if not os.path.exists(self.db_path):
            self._create_database()
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def _create_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            );
        ''')
        conn.commit()
        conn.close()

    def get_connection(self):
        if not self.conn:
            self.connect()
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn: Optional[Connection] = None

