# Inserindo Flask
from flask import Flask, render_template, request, redirect, url_for

#Inserindo MySQL
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            database = "escola",
            user = "root",
            password = ""
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

@app.route("/")
def index():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("Select * from alunos")
        alunos = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('index.html', alunos=alunos)