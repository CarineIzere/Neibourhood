# TITLE

     NEIGHBOURHOOD

# BUILT BY
     Carine Izere
# DESCRIPTION

       This is a web application that allows you to be in the loop about everything happening in your neighborhood.

 ## Live Demo

https://carineyi.herokuapp.com/

# INSTALATION REQUIREMENTS

        installations required
        python version should be 3.6 -Django version 1.11 pip install django==1.11
        Additionally, you’ll need to make sure you have pip available. You can check this by running:
        pip --Version
        `Install Pipenv pip install --user pipenv
        `install virtualenv and then test it
        python3.6 pip install --user --upgrade pip
        python3.6 -m virtualenv env
        source env/bin/activate

## Inorder to clone , follow the procedure below;

        On GitHub, navigate to the main page of the repository.
        Under the repository name, click Clone or downlonload.
        click the paste button.
        Open Terminal.
        Change the current working directory to the location where - you want the cloned directory to be made.
        Type git clone, and then paste the URL you copied in Step 2.
        git clone https://github.com/CarineIzere/Neighbourhood.git Press Enter.

#  CREATING A DATABASE

        psql
        CREATE DATABASE neyi;
        connect to the database \c neyi;
        check if tables have been created \dt

#  RUN MIGRATIONS

        python3.6 manage.py migrate
        python3.6 manage.py makemigrations neighbour

#  RUNNING THE APP

        python3.6 manage.py runserver

#  TESTING

        python3.6 manage.py test neighbour

# TECHNOLOGIES USED

- Python 3.6
- Django MVC framework
- HTML, CSS and Bootstrap
- JavaScript
- Postgressql
- Heroku

# Prerequisites 

`python3.6 pip virtualenv 
`Cloning In your terminal:

`$git clone https://github.com/CarineIzere/Award_Project/ 
`$cd Instagram
`Running the Application 
`Creating the virtual environment

`$python3.6 -m venv --without-pip virtual $ 
`source virtual/bin/env 
`Installing Django. 
`(virtual)$ pip install django==1.11
`Confirm that you do have Django.
`To achieve this, activate your python shell and run python3.6 on your terminal.
`Under your shell input this code:
 >>> import django
>>> django.get_version()
'1.11.5'
`Start a Django server.
`(virtual)$ python3.6 manage.py runserver
`Performing system checks...

`System check identified no issues (0 silenced).
September 28, 2018 - 12:01:08
Django version 1.11, using settings 'gallery.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

## Known bugs, 

No known bugs

## support and Contacts

Incase of any bugs contact me at carizeree@gmail.com or call on +250783706421

## License Copyright (c) 2019 Carine Izere

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
