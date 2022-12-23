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
                1. adding bootstrap starter template and navbar
             2. about.html
          3. static (in this static directory we can add our own css/js/images)
             1. css
                1. style.css
                   1. crating a css class `nav-bar` for background color of navbar
                   2. copying this https://uigradients.com/#Nelson gradient color from this cool website, click on `<>` button and copy the entire code ![img_1.png](img_1.png)
                   3. now, link this css file with index.html otherwise it will not work
                      1. to link css file in html file add this line of code `<link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/style.css') }}">` in below under the head tag and below the meta tag
                      ```
                        <head>
                        <!-- Required meta tags -->
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    
                        <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='css/style.css') }}">
                      ```
                      2. `"{{ url_for('static',filename='css/style.css') }}"` this is python code to link the external files
                         1. `{{  }}` using this curly braces (with one space end beginning and end) write python script in html, `url_for()` flask fn to link files, static` folder name which want to link, then filename
       2. Now, run `main.py`
       3. Result: 
          1. on homepage: http://127.0.0.1:5000/  
              ![img.png](img.png)
          
          
                    
            
## Git Push Commands
1. `git init` to initialize repo
2. `git add .` adding files 
3. `git commit -m "Add existing project files to Git"` stagging 
4. `git remote add origin https://github.com/cameronmcnz/example-website.git` (optionl assiging repo )
5. `git status` to check stagging/added files status
6. `git push -u -f origin master` final push to git
