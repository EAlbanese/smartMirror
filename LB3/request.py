from flask import Flask, request
import requests
import mariadb
import json
import os
from datetime import date

app = Flask(__name__)

conn = mariadb.connect(
    user="weather",
    password="root",
    host="localhost",
    database="smartMirror")

class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

@app.route('/weather', methods = ["POST"])
def post():
    data = request.get_json()
    cur = conn.cursor()
    try: 
        cur.execute("INSERT INTO weather (temp,hum) VALUES ("+str(data["temp"])+", "+str(data["hum"])+")")
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()

    return str(cur.lastrowid)

@app.route('/user', methods = ["POST"])
def post():
    cur = conn.cursor()  
    username = os.getlogin()
    today = date.today()
    todo_name = "test"
    try: 
        cur.execute("INSERT INTO user (username, todo_name, todo_Date) VALUES ("+username+", "+todo_name+", "+str(today)+")")
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()

    return str(cur.lastrowid)


@app.route('/weather', methods = ["GET"])
def get():
    cur = conn.cursor()  
    cur.execute("SELECT hum, temp, DATE_FORMAT(date, '%Y-%m-%d %h:%m:%s') FROM weather")
    rv = cur.fetchall()
    response = []
    for row in rv:
        response.append({"temp":row[0],"hum":row[1],"date":row[2]})
    return app.response_class(
        response = json.dumps(response),
        status = 200,
        mimetype='application/json'
    )  

@app.route('/user', methods = ["GET"])
def get():
    cur = conn.cursor()  
    cur.execute("SELECT username, todo_name, todo_Date FROM user")
    rv = cur.fetchall()
    response = []
    for row in rv:
        response.append({"username":row[0],"todo_name":row[1],"todo_Date":row[2]})
    return app.response_class(
        response = json.dumps(response),
        status = 200,
        mimetype='application/json'
    )  
 
app.run(host='0.0.0.0')
