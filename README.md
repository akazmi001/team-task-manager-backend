# Task Manager — Backend Setup Guide

## Prerequisites

- Python 3.8+
- MySQL Server
- pip

---

## 1. Create Virtual Environment

```bash
python -m venv env
```

---

## 2. Activate Virtual Environment

**Command Prompt (CMD):**
```bash
source env\bin\activate.bat
```

**PowerShell:**
```powershell
.\env\Scripts\activate.ps1
```

> ⚠️ If PowerShell blocks the script, run this first:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

## 3. Install Dependencies

Make sure you are at the project root folder (the one containing `requirements.txt`), then run:

```bash
pip install -r requirements.txt
```

---

## 4. Install MySQL Server

If you don't have MySQL installed, download and install it from:
👉 https://dev.mysql.com/downloads/mysql/

---

## 5. Create the Database

Open your MySQL client and run:

```sql
CREATE DATABASE task_manager;
```

Use the following database credentials in your Django settings:

| Field    | Value       |
|----------|-------------|
| Name     | task_manager |
| User     | root        |
| Password | dekho@123   |

> 💡 If your MySQL `root` user has no password, leave the `PASSWORD` field as an empty string `""` in `settings.py`.

Your `DATABASES` config in `settings.py` should look like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'task_manager',
        'USER': 'root',
        'PASSWORD': 'dekho@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 6. Run the Development Server

Make sure you are at the project root folder (the one containing `manage.py`), then run:

```bash
python manage.py runserver
```

The server will start at:
```
http://127.0.0.1:8000/
```

---

## Quick Start Summary

```bash
# 1. Create environment
python -m venv env

# 2. Activate (PowerShell)
.\env\Scripts\activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run server
python manage.py runserver
```

---

## Troubleshooting

**`activate.ps1 cannot be loaded` error**
Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy RemoteSigned
```

**MySQL connection refused**
Make sure MySQL service is running:
```bash
# Windows
net start mysql

# macOS/Linux
sudo service mysql start
```

**Missing migrations**
If you get database errors on first run:
```bash
python manage.py migrate
```