# TODO-Using-Django

Basic TODO app in which different users can login and add their own TODO with APIS


## Setup Instructions

Clone the repo in your local system

```bash
  git clone https://github.com/prabs222/TODO-Using-Django.git
```
Install virtualenv

```bash
  py -m pip install --user virtualenv
```
Create a new Virtualenvironment

```bash
  py -m venv env
```
Activate the Virtualenvironment with

```bash
  .\env\Scripts\activate
```
Change directory to the folder

```bash
  cd folder-where-you-cloned-the-repo
```

Apply all the migrations with 

```bash
  python3 manage.py migrate
```
Run the developement server with 

```bash
  python3 manage.py runserver
```
You'll see output like this
```bash
  Performing system checks...

System check identified no issues (0 silenced).
July 04, 2022 - 15:50:53
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Creating Superuser

Clone the repo in your local system

```bash
python3 manage.py createsuperuser
```
You will see a screen like this

```bash
Username (leave blank to use 'default'):
```
Enter a username and press enter , you will see a screen like this

```bash
Email address:
```
Enter an email and press enter , then you will see a screen like this

```bash
Password:
```
Enter a password , then you will see a screen like this

```bash
Password (again):
```
Re-enter the password and you are done! You will see a screen like this

```bash
Superuser created successfully
```

## Tech Stack

**Client:** HTML , CSS , Javascript

**Server:** Django , Python

## Features

- CRUD operation on TODO




[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


##
([@prabs222](https://github.com/prabs222))
