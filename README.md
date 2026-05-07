backend:
1.create environtment
    command >> python - m venv env
2. activate environment
    in cmd:
        source env\bin\activate.bat
    in powershell:
     .\env\Scripts\activate.ps1
3. install dependancies[ensure you are at project root folder which contain requirements.txt file]
    command > pip install -r requirements.txt
4. install mysql - server[if not have already]
5. create database with below info:
    name: "task_manager"
    user: "root"
    "PASSWORD": "dekho@123"  // if user have any password then write exact here else keep it blank
6. run server for backend [ensure you are at project root folder which contain manage.py file]
    command>> python manage.py runserver