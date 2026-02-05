from flask import Flask
import mysql.connector
import os
app=Flask(__name__)

db=mysql.connector.connect(host="db",user=os.getenv("MYSQL_USER"),password=os.getenv("MYSQL_PASSWORD"),database=os.getenv("MYSQL_DATABASE"))

@app.route("/")
def home():
    return "Enterprise Docker App - Backend is Running"

@app.route("/health")
def health():
    return {"Status":"UP"}

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
