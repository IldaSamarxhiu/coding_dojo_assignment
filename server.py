from flask import Flask, render_template, redirect, request
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='users_schema',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def read_all():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
    connection.close()
    return render_template('read_all.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s);"
        cursor.execute(sql, (first_name, last_name, email))
        connection.commit()
    connection.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


