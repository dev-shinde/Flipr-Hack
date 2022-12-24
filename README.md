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

## Features added till here
1. Login,Register, Home and About page created
2. App load at login page
   1. from login page
      1. login > home page
      2. register page
      3. about page
   2. from register page
      1. register > home page
      2. login page
      3. about page
   3. from about page
      1. login page
3. Once a user logged-in 
   1. Can do
      1. Home page
      2. logout
   2. can't do
      1. cannot go to register page 
      2. cannot log-in in another tab if try to open login page will redirect to home page
4. After Register
   1. allowed
      1. go to home page
      2. logout
   2. not allowed
      1. try to login in another tab
      2. try to register in another tab
5. Logout
   1. logout from home page
   2. if it is logged-in in another page after any action it will automatically logout

6. Auto session timeout is max 5minutes 
   1. if no longer active after 5 mins it will be logged-out and session time will be expired
                
   
## Update
1. Connected with new database
2. Add new Expense collapse form created
          
                    
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
6. `git push -u -f origin master` final push to git
