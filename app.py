
from flask import Flask, render_template, request, redirect, abort
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="mysqluser",
    password="innovatron@123",
    database="flask_app"
)
cursor = db.cursor(dictionary=True)

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/users')
def list_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        db.commit()
        return redirect('/users')
    return render_template('new_user.html')

@app.route('/users/<int:user_id>')
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    if not user:
        abort(404, "User not found")
    return render_template('user_profile.html', user=user)

@app.errorhandler(404)
def page_not_found(e):
    return f"<h1>404</h1><p>{e.description}</p>", 404

if __name__ == '__main__':
    app.run(debug=True)
