import os

from flask import Flask

app = Flask(__name__)

DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')


@app.route("/")
def hello_world():
    return f"""
    <p>Hello, World!</p>
    <p>---something important from environ---</p>
    <p>DB_NAME={DB_NAME}</p>
    <p>DB_USERNAME={DB_USERNAME}</p>
    <p>DB_PASSWORD={DB_PASSWORD}</p>
    <p>DB_HOST={DB_HOST}</p>
    <p>DB_PORT={DB_PORT}</p>
    """
