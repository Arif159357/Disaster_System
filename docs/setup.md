# Project Setup

A guide to setting up required dependencies to run the project.

## 1. Setting Up Virtual Environment

1. Create python virtual environment.

   - Create using the following command
     ```bash
     $ python3 -m venv venv
     ```
   - Activate virtual environment
     ```bash
     $ source venv/bin/activate # From project directory
     ```

2. Update pip to latest version using the following command:
   ```bash
   $ pip install --upgrade pip
   ```

## 2. Installing other dependencies

Install other dependecies from [requirements.txt](requirements.txt)

```bash
$ pip install -r requirements.txt
```

## 3. Running

Run the following after activating the virtual enviornment.

```
python manage.py migrate --run-syncdb
python manage.py makemigrations
python manage.py migrate
python3 manage.py runserver
```
