from flask import Flask, render_template, request, redirect, session, flash
import os
from datetime import timedelta  # used for setting session timeout
import pandas as pd
import plotly
import plotly.express as px
import json

import support

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def login():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)
    if 'user_id' in session:  # if logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')
    else:  # if not logged-in
        return render_template("login.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    if 'user_id' not in session:  # if user not logged-in
        email = request.form.get('email')
        passwd = request.form.get('password')
        query = """SELECT * FROM user_login WHERE email LIKE '{}' AND password LIKE '{}'""".format(email, passwd)
        users = support.execute_query("search", query)
        if len(users) > 0:  # if user details matched in db
            session['user_id'] = users[0][0]
            return redirect('/home')
        else:  # if user details not matched in db
            flash("Invalid email and password!")
            return redirect('/')
    else:  # if user already logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')


@app.route('/reset', methods=['POST'])
def reset():
    if 'user_id' not in session:
        email = request.form.get('femail')
        pswd = request.form.get('pswd')
        userdata = support.execute_query('search', """select * from user_login where email LIKE '{}'""".format(email))
        print(userdata)
        if len(userdata) > 0:
            try:
                query = """update user_login set password = '{}' where email = '{}'""".format(pswd, email)
                support.execute_query('insert', query)
                flash("Password has been changed!!")
                return redirect('/')
            except:
                flash("Something went wrong!!")
                return redirect('/')
        else:
            flash("Invalid email address!!")
            return redirect('/')
    else:
        return redirect('/home')


@app.route('/register')
def register():
    if 'user_id' in session:  # if user is logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')
    else:  # if not logged-in
        return render_template("register.html")


@app.route('/registration', methods=['POST'])
def registration():
    if 'user_id' not in session:  # if not logged-in
        name = request.form.get('name')
        email = request.form.get('email')
        passwd = request.form.get('password')
        if len(name) > 5 and len(email) > 10 and len(passwd) > 5:  # if input details satisfy length condition
            try:
                query = """INSERT INTO user_login(username, email, password) VALUES('{}','{}','{}')""".format(name,
                                                                                                              email,
                                                                                                              passwd)
                support.execute_query('insert', query)

                user = support.execute_query('search',
                                             """SELECT * from user_login where email LIKE '{}'""".format(email))
                session['user_id'] = user[0][0]  # set session on successful registration
                flash("Successfully Registered!!")
                return redirect('/home')
            except:
                flash("Email id already exists, use another email!!")
                return redirect('/register')
        else:  # if input condition length not satisfy
            flash("Not enough data to register, try again!!")
            return redirect('/register')
    else:  # if already logged-in
        flash("Already a user is logged-in!")
        return redirect('/home')


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/home')
def home():
    if 'user_id' in session:  # if user is logged-in
        query = """select * from user_login where user_id = {} """.format(session['user_id'])
        userdata = support.execute_query("search", query)

        table_query = """select * from user_expenses where user_id = {} order by pdate desc""".format(
            session['user_id'])
        table_data = support.execute_query("search", table_query)

        df = pd.DataFrame(table_data, columns=['#', 'User_Id', 'Date', 'Expense', 'Amount', 'Note'])
        df = support.generate_df(df)
        earning, spend, invest, saving = support.top_tiles(df)
        try:
            bar, pie, line, stack_bar = support.generate_Graph(df)
            monthly_data = support.get_monthly_data(df)
            card_data = support.sort_summary(df)
        except:
            bar, pie, line, stack_bar = None, None, None, None
            monthly_data = []
            card_data = []

        return render_template('home.html', user_name=userdata[0][1], earning=earning, spend=spend, invest=invest,
                               saving=saving, monthly_data=monthly_data, card_data=card_data,
                               table_data=table_data[:4], bar=bar, line=line,
                               stack_bar=stack_bar, pie=pie)
    else:  # if not logged-in
        return redirect('/')


@app.route('/home/add_expense', methods=['POST'])
def add_expense():
    if 'user_id' in session:
        user_id = session['user_id']
        if request.method == 'POST':
            date = request.form.get('e_date')
            expense = request.form.get('e_type')
            amount = request.form.get('amount')
            notes = request.form.get('notes')
            try:
                query = """insert into user_expenses (user_id, pdate, expense, amount, pdescription) values 
                ({}, '{}','{}',{},'{}')""".format(user_id, date, expense, amount, notes)
                support.execute_query('insert', query)
                flash("Saved!!")
            except:
                flash("Something went wrong.")
                return redirect("/home")
            return redirect('/home')
    else:
        return redirect('/')


@app.route('/analysis')
def analysis():
    if 'user_id' in session:  # if already logged-in
        query = """select * from user_login where user_id = {} """.format(session['user_id'])
        userdata = support.execute_query('search', query)

        query2 = """select expense, sum(amount) from user_expenses where user_id = {} group by expense order by expense""".format(
            session['user_id'])

        data = support.execute_query('search', query2)
        df = pd.DataFrame(data, columns=['Expense', 'Amount'])

        if df.shape[0] > 1:
            bar = px.bar(x=df['Expense'], y=df['Amount'], color=df['Expense'],
                         labels={'x': 'Expense Type', 'y': 'Amount(Rs)'}, height=280)
            bar.update_layout(title_text='Expense Bar', title_x=0.5, margin=dict(l=2, r=2, t=30, b=2))
            bar.update(layout_showlegend=True)

            pie = px.pie(df, values='Amount', names='Expense', height=280)
            pie.update_layout(title_text='Pie Chart', title_x=0.5, margin=dict(l=2, r=2, t=30, b=2))

            graphJSON = json.dumps(bar, cls=plotly.utils.PlotlyJSONEncoder)
            graphJSON2 = json.dumps(pie, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('analysis.html', user_name=userdata[0][1], graphJSON=graphJSON,
                                   graphJSON2=graphJSON2)
    else:  # if not logged-in
        return redirect('/')


@app.route('/profile')
def profile():
    if 'user_id' in session:  # if logged-in
        query = """select * from user_login where user_id = {} """.format(session['user_id'])
        userdata = support.execute_query('search', query)
        return render_template('profile.html', user_name=userdata[0][1])
    else:  # if not logged-in
        return redirect('/')


@app.route('/logout')
def logout():
    try:
        session.pop("user_id")  # delete the user_id in session (deleting session)
        return redirect('/')
    except:  # if already logged-out but in another tab still logged-in
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
