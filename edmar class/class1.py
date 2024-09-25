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