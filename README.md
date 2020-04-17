# Profiles Rest API

### Business Requirements:

1. User Profile Login/Register and status update Rest API using Django Rest Framework
2. Using SQLite as the database

### Requirements:

-   python3
-   pip
-   python libraries:
    _ Django
    _ Django Rest Framework
-   git

## To run the application on your local machine:

### Clone the repository:

1. Type the following in your terminal

    `git clone https://github.com/pushp1997/profiles-rest-api.git`

2. Change the directory into the repository

    `cd ./profiles-rest-api`

3. Create python virtual environment

    `python3 -m venv ./drf-env`

4. Activate the virtual environment created

    - On linux / MacOS :
      `source ./drf-env/bin/activate`
    - On Windows (cmd) :
      `"./drf-env/Scripts/activate.bat"`
    - On Windows (powershell) :
      `"./drf-env/Scripts/activate.ps1"`

5. Install python requirements

    `pip install -r requirements.txt`

6. Run Server

    `python manage.py runserver 0.0.0.0:8000`

### API endpoints:

1. /api/hello-view/ (using APIView)

    - GET:

    ```
    Little description about APIView
    ```

    - PUT:

    ```
    {
        "name" : "Enter your name here"
    }
    ```

2. /api/hello-viewset/ (using ViewSet)

    - GET:

    ```
    Little description about ViewSet
    ```

    - PUT:

    ```
    {
        "name" : "Enter your name here"
    }
    ```

3. /api/profile/ (using ViewSet)

    - GET:

    ```
    List of all User Profiles
    ```

    - PUT:

    ```
    {
        "email": "",
        "name": "",
        "password": ""
    }
    ```

4. /api/profile/{primary_key}/

    - GET:

    ```
    Get the user profile with matching primary key
    ```

    - POST:

    ```
    Users can update their own profile only. In header provide 'Authorization' as key and 'Token {Authentication token}' as the value
    {
        "email": "",
        "name": "",
        "password": ""
    }
    ```

    - PATCH:

    ```
    Users can partialy update their own profile only. In header provide 'Authorization' as key and 'Token {Authentication token}' as the value
    {
        "email": "",
        "name": "",
        "password": ""
    }
    ```

    - DELETE:

    ```
    Users can delete their own profile only. In header provide 'Authorization' as key and 'Token {Authentication token}' as the value
    ```

5. /api/login/

    - PUT:

    ```
    {
        "username": "Email address goes here",
        "password": "Password goes here"
    }
    On success the response will have authorization token
    ```
