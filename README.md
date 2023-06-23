
# Django App Setup

- The purpose of this app was to practice Django by creating a simple to-do list that does all the basic crud operations. I've added extensive documentation in each file to explain the logic of the code.

- All list to-do items will be saved to a database. This app will be using the MySQL desktop app as its database.

- This project will mainly serve as a guide for future projects.









### Project Setup

- This guide walks you through the setup process for creating a Django app.
### 🔴Prerequisites:
- Python 
- Django ```pip install Django```
- [MySQL Desktop](https://www.mysql.com/products/workbench/)
### 🟢 Create a Django project:
- Open a terminal or command prompt, navigate to the directory where you want to create your Django project, and run the following command to create a new Django project:
```
django-admin startproject project_name
```
- This will create a new directory named **project_name** with the basic Django project structure.



    
### 🟢 Configure MySQL database settings:
- Open the **settings.py** file located in the **project_name** directory and find the DATABASES section. Update the configuration as follows:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'your_mysql_host e.g.127.0.0.1',
        'PORT': 'your_mysql_port e.g.3306',
    }
}
```
### 🔵 Start the MySQL server:
- Launch the MySQL ***Desktop app*** and start the MySQL server. Ensure that the server is running on the default port 3306.

### 🔵 Create a MySQL database: 
- In the MySQL ***Desktop app***, open a new connection to your local MySQL server. Once connected, create a new database by executing the following SQL query:
```
CREATE DATABASE your_database_name;
```
- Replace 'your_database_name' with the same name you specified in the Django project's **settings.py** file.

### 🔵 Run database migrations: 
- In the terminal or command prompt, navigate to the **project_name** directory and run the following command to apply the initial database migrations:
### 🔵 Run database migrations:
- In the terminal or command prompt, navigate to the **project_name** directory and run the following command to apply the initial database migrations:
```
python manage.py migrate

```
- This will create the necessary database tables for Django's default applications.
- In Django, a migration is a way to manage changes to your project's database schema over time. It allows you to evolve the structure of your database as your application's models change.
- Migrations help you handle tasks such as creating new tables, modifying existing tables, adding or removing columns, and establishing relationships between tables.
- When you define or modify a model in Django, Django's built-in migration system automatically generates migration files. These files, located in the migrations directory of each app, contain Python code that describes the changes to be made to the database.
### 🟢 Create Django app:
- To create a new Django app within your project, run the following command:
```python
python manage.py startapp myapp

```
- Replace 'myapp' with the desired name of your app.

#### After creating the app, you should follow these additional steps to configure the app in your project:

- Open the **settings.py** file located in the project's directory (the same directory where manage.py is located).

- Locate the **INSTALLED_APPS** list in the **settings.py** file. This list contains the names of all the apps installed in your Django project.

- Add your app's name, **'myapp'**, to the **INSTALLED_APPS** list. It should look something like this:
```
INSTALLED_APPS = [
    ...
    'myapp',
]

```

- By adding your app's name to the **INSTALLED_APPS** list, you are telling Django to include your app in the project and consider it for migrations and other functionalities.

- Save the **settings.py** file after making the changes.

- By adding your app's name to the **INSTALLED_APPS** list in **settings.py**, you are instructing Django to recognize and include your app when performing various operations, including migrations, URL routing, and template loading.


### 🟢 Define models:

- Open the **models.py** file inside the newly created myapp directory and define your database models using Django's model syntax. Refer to the [Django documentation](https://docs.djangoproject.com/en/3.2/topics/db/models/) for detailed information on defining models.
### 🔵 Generate and apply migrations
- Run the following command to generate the migrations for your app's models:
```python
python manage.py makemigrations myapp
```
- Before applying the actual changes to the database, you need to create the migration files. You can generate these files by running the command ***python manage.py makemigrations***. Django analyzes your models and generates the necessary migration files based on the changes detected.

### 🔵 Then apply the migrations to update the database schema:
- Once the migration files are created, you can apply them to the database using the python ***manage.py migrate*** command. This command reads the migration files and executes the SQL statements required to bring the database schema up to date. It creates tables, modifies columns, adds indexes, and performs other necessary database operations.

- In summary, python manage.py migrate is a Django command that applies database migrations, which are changes to your database schema defined by your models, to keep your database structure in sync with your Django project.

```python
python manage.py migrate
```


### 🟢 Start the development server:
- Start the Django development server by running the following command:
```python
python manage.py runserver
```
- The server should start running on http://127.0.0.1:8000/. Leave the server running while you work on your project.
- Access your Django app: Open a web browser and visit http://127.0.0.1:8000/ or http://localhost:8000/. You should see the default Django landing page if everything is set up correctly.

## That's it💥

## Additional Configuration (Optional)
- If you want to create an administrative user to access the Django admin interface, run the following command and follow the prompts:
```python
python manage.py createsuperuser
```

## Setting Up CSS in all Django HTML Files:

- Open your Django project in your preferred code editor.

- Make sure that **django.contrib.staticfiles** is included in your **INSTALLED_APPS** setting. Open the **settings.py** file in your project directory.

- Locate the **INSTALLED_APPS** setting in the **settings.py** file.

- Add **'django.contrib.staticfiles'** to the list of installed apps if it's not already present. The updated **INSTALLED_APPS** setting should look like this:

```
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    ...
]
```

- Define the **STATIC_URL** setting in the **settings.py** file. The **STATIC_URL** setting specifies the URL prefix to use for serving static files.

```
STATIC_URL = 'static/'
```
- Create a folder called **static** in your app directory (e.g., **my_app/static**). This is where you'll store your static files, including the **style.css** file.

- Place your **style.css** file inside the **static** folder. For example, the file path should be **my_app/static/style.css**.

- Open the HTML template file(s) where you want to apply the styles from **style.css**.

- Load the static template tags at the top of the HTML template file(s). Add the following line:
```html
{% load static %}
```

- Use the **static** template tag to reference the **style.css** file in your HTML template. Inside the appropriate HTML tag, add the following line:

```html
<link rel="stylesheet" href="{% static 'style.css' %}">

```
- This line will generate the correct URL to the **style.css** file based on the **STATIC_URL** setting.

- Finally, Start the Django development server. 