# Store API

Simple store API, using Django REST Framework.

## How to use

I used pipenv as environment handler. Feel free to use any other.

You can find some useful commands to set up the application on localhost, just type ``make`` on the console and you will find:

```bash

run                 Test api 
admin               Create admin user 
install_dep         Install Python Dependencies from requirements.txt file 
commit              Commit changes 
migrations          Make models migrations 

```

## Available paths

    admin/
    accounts/
    accounts/register/
    accounts/login/
    accounts/logout/
    api/token/
    api/token/refresh/
    api/token/verify/