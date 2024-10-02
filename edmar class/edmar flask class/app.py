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
    else:
        return "Erro na conexão com o Banco de Dados."

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        turma = request.form['turma']
        
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            inserir_query = "INSERT INTO alunos (nome,idade,turma) VALUES (%s,%s,%s)"
            dados = (nome, idade, turma)
            cursor.execute(inserir_query, dados)
            connection.commit()
            cursor.close()
            return redirect(url_for('index'))
        else:
            return 'Erro na conexão com o Banco de Dados.'
    return render_template('adicionar_aluno.html')