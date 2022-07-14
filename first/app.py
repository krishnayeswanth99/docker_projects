import json
from flask import Flask
import mysql.connector
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/initdb')
def db_init():
    conn = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="secret",
        port="3306"
    )
    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS first")
    cursor.execute("CREATE DATABASE first")

    cursor.close()

    conn = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="secret",
        database="first",
        port="3306"
    )
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS first.first")
    cursor.execute("CREATE TABLE first (name VARCHAR(255), address VARCHAR(255))")

    return "Created Successfully!!"


@app.route('/list')
def list_table():
    conn = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="secret",
        database="first",
        port="3306"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * from first")

    headers = [x[0] for x in cursor.description]
    myresult = cursor.fetchall()
    json_data = []
    for res in myresult:
        json_data.append(dict(zip(headers, res)))

    return json.dumps(json_data)
