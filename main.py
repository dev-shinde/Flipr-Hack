from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector  # pip install mysql-connector-python
import os
from datetime import timedelta  # used for setting session timeout
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)
app.secret_key = os.urandom(24)
conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", port=3306, database='expense',
                               auth_plugin='mysql_native_password')
cursor = conn.cursor()


@app.route('/')
def login():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'user_id' in session:  # if logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')
    else:  # if not logged-in
        return render_template("login.html")


@app.route('/register')
def register():
    if 'user_id' in session:  # if user is logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')
    else:  # if not logged-in
        return render_template("register.html")


@app.route('/home')
def home():
    if 'user_id' in session:  # if user is logged-in
        cursor.execute("""select * from user_login where user_id = {} """.format(session['user_id']))
        userdata = cursor.fetchall()
        return render_template('home.html', user_name=userdata[0][1])
    else:  # if not logged-in
        return redirect('/')


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    if 'user_id' not in session:  # if user not logged-in
        email = request.form.get('email')
        passwd = request.form.get('password')
        cursor.execute("""SELECT * FROM user_login WHERE email LIKE '{}' AND password LIKE '{}'""".format(email, passwd))
        users = cursor.fetchall()
        if len(users) > 0:  # if user details matched in db
            session['user_id'] = users[0][0]
            return redirect('/home')
        else:  # if user details not matched in db
            flash("Invalid email and password!")
            return redirect('/')
    else:  # if user already logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')


@app.route('/registration', methods=['POST'])
def registration():
    if 'user_id' not in session:  # if not logged-in
        name = request.form.get('name')
        email = request.form.get('email')
        passwd = request.form.get('password')
        if len(name) > 5 and len(email) > 10 and len(passwd) > 5:  # if input details satisfy length condition
            try:
                cursor.execute(
                    """INSERT INTO user_login(username, email, password) VALUES('{}','{}','{}')""".format(name, email,
                                                                                                          passwd))
                conn.commit()
            except Exception as e:
                print(e)
            cursor.execute("""SELECT * from user_login where email LIKE '{}'""".format(email))
            user = cursor.fetchall()
            session['user_id'] = user[0][0]  # set session on successful registration
            flash("Already a user is logged-in!")
            return redirect('/home')
        else:  # if input condition length not satisfy
            return redirect('/register')
    else:  # if already logged-in
        return redirect('/home')


@app.route('/analysis')
def analysis():
    if 'user_id' in session:  # if already logged-in
        cursor.execute("""select * from user_login where user_id = {} """.format(session['user_id']))
        userdata = cursor.fetchall()
        students = [['Savings', 24000, 'Sydney', 'Australia'],
                    ['Spends', 20000, 'Coimbatore', 'India'],
                    ['Investments', 15000, 'Coimbatore', 'India'],
                    ['Earnings', 56000, 'Tokyo', 'Japan']]

        # Convert list to dataframe and assign column values
        df = pd.DataFrame(students,
                          columns=['Expense', 'Amount', 'City', 'Country'],
                          index=['a', 'b', 'c', 'd'])

        fig = px.bar(df, x='Expense', y='Amount', color='City', barmode='group')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template('analysis.html', user_name=userdata[0][1], graphJSON=graphJSON)
    else:  # if not logged-in
        return redirect('/')


@app.route('/profile')
def profile():
    if 'user_id' in session:  # if logged-in
        cursor.execute("""select * from user_login where user_id = {} """.format(session['user_id']))
        userdata = cursor.fetchall()
        return render_template('profile.html', user_name=userdata[0][1])
    else:  # if not logged-in
        return redirect('/')


@app.route('/logout')
def logout():
    try:
        session.pop("user_id")  # delete the user_id in session (deleting session)
        return redirect('/')
    except: # if already logged-out but in another tab still logged-in
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
