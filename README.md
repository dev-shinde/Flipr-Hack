# Flask_Expense_App
Creating a simple Expense Track app using Flask and Python

1. Create New Repository in Github as `Flask_Expense_App`
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
                * simple Homepage designed in this ![img.png](img.png)
          3. static 
             1. css
                1. style.css
4. Login Functionality 
   1. send the login form data though `post`
      * in `index.html` 
      ```
       <form class="form" method="post" action="/login_validation">
         <label>Email</label><br>
         <input type="email" class="form-control" name="email" placeholder="Enter your registered email"><br>
         <label>Password</label><br>
         <input type="password" class="form-control" name="password" placeholder="Enter your password"><br><br>
         <input type="submit" class="btn btn-primary btn-block btn-lg" value="Login">
       </form>
      ```
   2. Login Functionality
      * once the submit button clicked the form data with name email and password will be sent through `post` method to `action='/login_validation'` (a route where data will receive)
        * receiving data at this route using post `main.py`
        * it will receive data using `request` function
          ```
          from flask import request
          @app.route('/login_validation',methods=['POST']) #where and how will receive data
          def login_validation():
            email = request.form.get('email') # receiving form data email and string in email variable, this 'email' keyword should be same as in index.html form name 
            passwd = request.form.get('password') # receiving form data password and storing in passwd varibale  this 'password' keyword should be same as in index.html form name
            return f"Email : {email} and Password: {passwd}"
          ```
          
   - Test: Form data submit 
     ![img.png](img.png)
   
   - received data /login_validation:
     ![img_1.png](img_1.png)
        
                
       
          
          
          
                    
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
6. `git push -u -f origin master` final push to git
