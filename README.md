# Store API

Simple store API, using Django REST Framework.

## How to use

I used pipenv as environment handler. Feel free to use any other.

If you are using pipenv, type:

    pipenv shell
    pipenv install

After that, you can use the commands mentioned below.


You can find some useful commands to set up the application on localhost, just type ``make`` on the console and you will find:

```bash

run                 Test api 
admin               Create admin user 
install_dep         Install Python Dependencies from requirements.txt file 
commit              Commit changes 
migrations          Make models migrations 

```

## Available paths

    admin/                  Admin UI     
    accounts/register/      Register new user
    accounts/login/         Login view
    accounts/logout/        Logout View
    accounts/upload-csv/    Upload users from csv file
    api/token/              Get JWT Token
    api/token/refresh/      Renew time for JWT Token expired
    api/token/verify/       Verify if JTW Token is valid
    api/products/           List all products
    api/bills/              List all bills



## Mocks

You can find mocks to use in ``mocks`` folder. Available mocks are:

*   Products mock (100 rows)
*   Users mock (1000 rows)

## DB Settings

By default, the api is connected with SQLlite, but includes PostgreSQL support, if you want to use this, take care to set the variables listed on the ``.env.sample`` file.

