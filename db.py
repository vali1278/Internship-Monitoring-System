import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="internship_monitoring"
)

cursor = db.cursor()
