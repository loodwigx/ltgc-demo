import sqlite3
from functools import reduce

def init_db():
  # TODO probably would be better if we persisted the db connection
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  create_address_table = """CREATE TABLE IF NOT EXISTS address (
                              address_id INTEGER PRIMARY KEY,
                              address TEXT NOT NULL,
                              city TEXT NOT NULL,
                              company TEXT DEFAULT '',
                              name TEXT NOT NULL,
                              state TEXT NOT NULL,
                              zip TEXT NOT NULL);"""
  cursor.execute(create_address_table)
  # TODO add some damn indexes you madman!
  conn.commit()
  cursor.close()
  print("database initialized")

def create_address(data):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  create_address_query = """INSERT INTO address (address, city, company, name, state, zip)
                            VALUES(?, ?, ?, ?, ?, ?);"""
  values = (data["address"], data["city"], data["company"],
             data["name"], data["state"], data["zip"])
  cursor.execute(create_address_query, values)
  conn.commit()
  cursor.close()
  return

def read_address(address_id):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  read_address_query = """SELECT address, city, company, name, state, zip
                          FROM  address
                          WHERE address_id=?
                          ORDER BY name;"""
  cursor.execute(read_address_query, address_id)
  record = cursor.fetchone()
  if record is None:
    raise ValueError
  keys = ("address", "city", "company", "name", "state", "zip")
  results = dict(zip(keys, record))
  cursor.close()
  return results

def read_addresses():
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  read_addresses_query = """SELECT address_id, address, city, company, name, state, zip
                            FROM  address
                            ORDER BY name;"""
  cursor.execute(read_addresses_query)
  records = cursor.fetchall()
  keys = ("address_id", "address", "city", "company", "name", "state", "zip")
  results = list(map(lambda row: dict(zip(keys, row)), records))
  cursor.close()
  return results

def update_address(address_id, data):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  update_address_query = """UPDATE address
                            SET address = ?,
                                city = ?,
                                company = ?,
                                name = ?,
                                state = ?,
                                zip = ?
                            WHERE address_id=?;"""
  values = (data["address"], data["city"], data["company"],
             data["name"], data["state"], data["zip"], address_id)
  cursor.execute(update_address_query, values)
  conn.commit()
  cursor.close()
  return

def delete_address(address_id):
  conn = sqlite3.connect('database.db')
  cursor = conn.cursor()
  update_address_query = """DELETE FROM address
                            WHERE address_id=?;"""
  cursor.execute(update_address_query, address_id)
  conn.commit()
  cursor.close()
  return
