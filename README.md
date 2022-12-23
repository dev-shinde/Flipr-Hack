# Flask_Expense_App
Creating a simple Expense Track app using Flask and Python

1. Create New Repository in GitHub as `Flask_Expense_App`
2. Clone this repo in local env `git repo https://github.com/santos-k/Flask_Expense_App.git`
3. Open VS Code or Pycharm
    1. Open the Project
       1. File and Directory structure
          1. `main.py`
          2. templates
             1. index.html
             2. register.html
             3. about.html
             4. home.html
          3. static 
             1. css
                1. style.css

# Problems 
   1. Homepage is accessible without login (in any browser in any tab), it should be not accessible without login
   2. After login in one tab login page accessible in another tab (in one browser only one user can login at a time)
   3. validation routes are visible in url bar

# Solution for 1. After login in one tab login page accessible in another tab
### if a user logged-in and session is active then he/she can't go to login page or register page in another tab of same window 
1. If user already logged-in and session(a dictionary of flask) is active and then try to go login page or register, will be redirected to home page
2. we will check if `user_id` present in session then will redirect to home page if user_id not present in session then only able to visit login or register page
 
   ```
    @app.route('/')
    def login():
        # if user is already logged in same browser and session is active then redirect to homepage else redirect to login page
        if 'user_id' in session:
            return redirect("/home")
        else:
            return render_template("index.html")
    
    
    @app.route('/register')
    def register():
        # if user is already logged in same browser and session is active then redirect to homepage else redirect to register page
        if 'user_id' in session:
            return redirect("/home")
        else:
            return render_template("register.html")
    ```
                
       
          
          
          
                    
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
6. `git push -u -f origin master` final push to git
