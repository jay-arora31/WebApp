
# WebApp


```plaintext
mainproject/
│
├── webapp/
│   ├── admin.py
│   ├── app.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── mainproject/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md

```

<h2>Setup :</h2>

Clone the repository to your local machine:
```sh
$ git clone https://github.com/jay-arora31/WebApp.git
$ cd WebApp
```
Install the required dependencies:
```sh
$ virtualenv venv
```
```sh
$ venv\scripts\activate


```
```sh
$ pip install -r requirements.txt


```

Apply database migrations:
```sh
$ python manage.py makemigrations


```
```sh
$ python manage.py migrate


```

Start the development server:
```sh
$ python manage.py runserver


```


### Output

![image](https://github.com/jay-arora31/WebApp/assets/68243425/12b9e054-0e95-41db-9119-b72ca5fcc595)

![image](https://github.com/jay-arora31/WebApp/assets/68243425/f8b94863-7343-4a7a-b006-af6668446213)

![image](https://github.com/jay-arora31/WebApp/assets/68243425/786b0a3c-493d-434c-abee-0e6b9cd07415)
