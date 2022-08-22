# api_final
##Running the project:
### Clone the repository:
```
git@github.com:KartashevaAnna/api_final_yatube.git
```
### Open it in your IDE and go to project folder:

```
cd yatube_api
```

### Create the virtual environment and activate it:

```
python -m venv env
```

```
venv\scripts\activate
```

### Install requirements:


```
pip install -r requirements.txt
```

### Apply migrations:

```
python manage.py migrate
```

### Run the server:

```
python manage.py runserver
```

##Developer:
###Anna Kartasheva

##Stack:
Djnago Rest Framework. For more details please see requirements.txt

##Available endpoints and request and reply examples:
The project has a number of endpoints. For example, you send a GET request 
to http://127.0.0.1:8000/api/v1/groups/, and you'll get a JSON response in the
following format:
{
"id": 0,
"title": "string",
"slug": "string",
"description": "string"
}
To get more examples, first run the project, then go to http://127.0.0.1:8000/swagger/.
