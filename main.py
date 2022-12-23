from flask import Flask, render_template, request

app = Flask(__name__)


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
    return f"Email : {email} and Password: {passwd}"


if __name__ == "__main__":
    app.run(debug=True)