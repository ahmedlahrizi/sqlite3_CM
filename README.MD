# SQLITE3 CM

SQLITE 3 CM is a context manager, 
😃
**A way TO USE `with` statement on sqlite databases !!**  (WITHOUT CLOSING OR OPENING ANYTING 🤩)

#  Docs 📄

```python
from sqlite3cm import OpenSqlite3db

with OpenSqlite3db(db_path="database.db", throw_error=True) as (conn, cursor):
	# SQL stuff here !
```

### Note:
You  shouldn't forget about the

## Arguments
`db_path`: Path to the **database**

`throw_error`:  Weather you want to throw an **error** or not

### Note:
**None** of these args are **required**.
____
# Lightness 🕊

## THE SCRIPT IS ONLY 20 LINES LONG 😄

# Features

At the **beggining**, the script will **connect to the database** and **create a cursor**

At the **end**, the script will **commit**, close the 