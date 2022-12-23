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

# Solution for 1. Homepage is accessible without login
 1. To know that a user logged in or not we need to track session by assigning a secret key to server and to the browser session,
 2. any user will be allowed to access homepage or any user related data page after only if the session secret key present in current session
 3. session key will only generate after successful login 
    1. session is special type of dictionary in flask
         ```
              from flask import session
              if len(users) > 0:
                  session['user_id'] = users[0][0] # storing user id 
                  return redirect('/home')
              else:
                  return redirect('/')
          ```
    2. Let's check session id without login, go to Inspect > Application > Cookies > this url ![img.png](img.png)
      
    3. Let's check session details after login ![img_1.png](img_1.png)
    4. Check in other tab session will be same ![img_2.png](img_2.png)
   
        
                
       
          
          
          
                    
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
6. `git push -u -f origin master` final push to git
