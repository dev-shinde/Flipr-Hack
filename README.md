# Flask_Expense_App
Creating a simple Expense Track app using Flask and Python

1. Create New Repository in Github as `Flask_Expense_App`
2. Clone this repo in local env `git repo https://github.com/santos-k/Flask_Expense_App.git`
3. Open VS Code
    1. Open the Project 
    2. Create a new `main.py` file
        1. test simple flask code with simple html code
            ```
            from flask import Flask

            app = Flask(__name__)

            @app.route('/')
            def home():
                return "<h1 style='color:red'>Hello World</h1>"

            if __name__ == "__main__":
                app.run(debug=True)
            ```
        2. Save and run this script, open VS terminal and run `python main.py`, open default url if not present in terminal http://127.0.0.1:5000/, generally default port 5000 assign to Flask.

        3. Output in browser `Hello Falsk` in red color
            
