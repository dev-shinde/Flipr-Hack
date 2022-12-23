from flask import Flask, render_template, request
import mysql.connector  # pip install mysql-connector-python

app = Flask(__name__)

# creating connection object with mysql
myconn = mysql.connector.connect(host="localhost", user="root", passwd="123456", port=3306, database='expense',
                                 auth_plugin='mysql_native_password')
cursor = myconn.cursor()


@app.route('/')
def login():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    passwd = request.form.get('password')
    cursor.execute("""SELECT * FROM EXPENSE_DETAILS WHERE EMAIL_ID LIKE '{}' AND USER_PASSWORD LIKE '{}'""".format(email,passwd))
    users = cursor.fetchall()
    # above code will return the one result in list of tuple
    print(users)
    if len(users) > 0:
        return render_template('home.html')
    else:
        return render_template('index.html')


@app.route('/registration',methods=['POST'])
def registration():
    name = request.form.get('name')
    email = request.form.get('email')
    passwd = request.form.get('password')
    if len(name)>5 and len(email)>10 and len(passwd)>5:
        cursor.execute("""INSERT INTO expense_details VALUES(NULL,'{}','{}','{}')""".format(name,email,passwd))
        myconn.commit()
        return f"Successfully Registered!!"
    else:
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
