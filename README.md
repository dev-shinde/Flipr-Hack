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

            @app.route('/about')
            def about():
                return "This is about page"

            if __name__ == "__main__":
                app.run(debug=True)
            ```
        2. Save and run this script, open VS terminal and run `python main.py`, open default url if not present in terminal http://127.0.0.1:5000/, generally default port 5000 assign to Flask.

        3. Output in browser at this home url http://127.0.0.1:5000/ or http://127.0.0.1:5000 will be `Hello Falsk` in red color
        4. Output at `/about` for url http://127.0.0.1:5000/about will be `This is about page` 
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
5. `git push -u -f origin master` final push to git