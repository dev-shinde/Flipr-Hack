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
4. Login Functionality 
   1. Login Functionality
      * once the submit button clicked the form data with name email and password will be sent through `post` method to this location `'/login_validation'` (a route where data will receive)
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


# Setup MySql for Database connection with python
   1. Install [Mysql](https://www.mysql.com/downloads/), not now the credentials open MySQL workbench, there will be usernmae, hostname, port no
      1. install mysql.connector package `pip install mysql-connector-python` refer [this video](mysql-connector-python) for mysql connection error 
            * Connect and test
              ```
              import mysql.connector  
              myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "123456",port=3306,database='expense', auth_plugin='mysql_native_password')
              cursor = myconn.cursor()
              cursor.execute("""select * from expense_details""")
              data = cursor.fetchall() # returns list of tuple of fetched rows
              for i in data:
                  print(i)
              ```
              * Output 
               ```
              (1, 'Santosh Kumar', 'santosh@gmail.com', 'Qwe123')
              (2, 'Upender Yadav', 'robinhud299@gmail.com', '12345')
              (3, 'Virat Kohali', 'virat@gmail.com', '12345')
              (4, 'MS Dhoni', 'msd7@gmail.com', '12345')
              (5, 'Santosh Yadav', 'sdsdsd@xcxc', '12345')
              ```
              setup completed
   2. Now, validating user login with database
      1. validation code: if we consider email as unique entry then combination of email and password will be unique result
         ```
         @app.route('/login_validation', methods=['POST'])
         def login_validation():
         email = request.form.get('email')
         passwd = request.form.get('password')
         cursor.execute("""SELECT * FROM EXPENSE_DETAILS WHERE EMAIL_ID LIKE '{}' AND USER_PASSWORD LIKE '{}'""".format(email,passwd))
         users = cursor.fetchall()
         # above code will return the one result in list of tuple
         if len(users) == 1:
            return f"Hello, {users[0][1]}"
         else: 
            return "Incorrect data"
         ```
   3. Test: 
      1. Entering correct data
         * ![img_3.png](img_3.png)
         * output:
           * ![img_4.png](img_4.png)
      2. Entering incorrect data 
         * ![img_5.png](img_5.png)
         * output 
           * ![img_6.png](img_6.png)

        
                
       
          
          
          
                    
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
6. `git push -u -f origin master` final push to git
