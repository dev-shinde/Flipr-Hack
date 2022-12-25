# Flask_Expense_App
Creating a simple Expense Track app using Flask and Python

1. Create New Repository in GitHub as `Flask_Expense_App`
2. Clone this repo in local env `git repo https://github.com/santos-k/Flask_Expense_App.git`
3. Open VS Code or Pycharm
    1. Open the Project
       1. File and Directory structure
          1. `main.py`
          2. templates
             1. login.html
             2. register.html
             3. contact.html
             4. home.html
             5. analysis.html
             6. profile.html
          3. static 
             1. css
                1. style.css

## Update
1. Add new expense record functionality added
2. Click Add New Record button, a model form will open, enter the details and submit
3. click outside the form to close the form
4. on successful update an alert message will appear for 3 seconds

## Database table schema

![img_4.png](img_4.png)

- Query to insert new record
```
 insert into user_expenses (user_id,pdate,expense,amount,pdescription) values (1, '2022-12-25','Spend',12212,'Room rest');
```
![img_5.png](img_5.png)


![img.png](img.png)
![img_1.png](img_1.png)
![img_2.png](img_2.png)
![img_3.png](img_3.png)

                    

## Freeze requirements.txt
save packages used in project, run below command to auto generate requirements.txt will all packages
`pip freeze > requirements.txt`
