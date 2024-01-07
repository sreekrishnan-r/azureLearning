from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World !!!"

if __name__ == "__main__":
    app.run(debug=True)
