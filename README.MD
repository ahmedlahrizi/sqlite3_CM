# [SQLITE3 CM](https://github.com/ahmedlahrizi/sqlite3_CM)
___
SQLITE 3 CM is a context manager, 
😃
**A way TO USE `with` statement on sqlite databases !!**  (WITHOUT CLOSING OR OPENING ANYTING 🤩)

# Install 📦
    pip install sqlite3cm

#  Docs 📄
___
```python
from sqlite3cm import OpenSqlite3db

with OpenSqlite3db("database.db", throw_error=True) as (conn, cursor):
    conn.execute('CREATE TABLE IF NOT EXISTS users')
```

### Note:
You shouldn't forget about the parentisis after the `as`

## Arguments
___
`db_path` Path to the **database** (can be **`Pathlib`** path) (default to "database.db")

`throw_error` Weather you want to throw an **error** or not (default to True)

### Note:
**None** of these arguments are **required**.

# Lightness 🕊
___
#### THE SCRIPT IS ONLY 20 LINES LONG 😄 (50 with docstrings and comments)

# Features 🧪
___
At the **beggining**, the script will **connect to the database** and **create a cursor**

At the **end**, the script will **commit**, close the connection and cursor