import sqlite3


class OpenSqlite3db:
    def __init__(self, db_path="database.db", throw_error=False):
        self.db = str(db_path)
        self.throw_error = throw_error

    def __enter__(self):
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def __exit__(self, ex_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        return self.throw_error
