from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sreekrishnan-flask-mysql-server.mysql.database.azure.com'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Admin@123'
app.config['MYSQL_DB'] = 'sreekrishnan-flask-mysql-database'

mysql = MySQL(app)

@app.route('/')
def example():
   with app.app_context():
      cursor = mysql.connection.cursor()
      cursor.execute('show databases')
      data = cursor.fetchall()
      cursor.close()
   print(len(data))
   
   return render_template('index.html', data_len = len(data), data=data)

if __name__ == "__main__":
    app.run(debug=True)
