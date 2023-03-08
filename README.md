# izzi API

This is a sample Django/Rest Framework API project that provides endpoints for a web app.

## Installation

To install this project, follow these steps:

1. Clone the repository to your local machine using the command `git clone https://github.com/kazimovzaman2/izzi-api.git`.
2. Install the required dependencies using the command `pip install -r requirements.txt`.
3. Create a new database using the command `python manage.py migrate`.
4. Run the development server using the command `python manage.py runserver`.

## Usage

To use this project, follow these steps:

1. Make requests to the API endpoints using tools like Postman or cURL.
2. Refer to the API documentation below for a list of available endpoints and their parameters.

## API Documentation

### Authentication Endpoints

- /api_auth/login/ (POST)
- /api_auth/register/ (POST)
- /api_auth/token-refresh/ (POST)
- /api_auth/update-user/ (GET, PUT)
- /api_auth/reset-password/ (POST)
- /api_auth/change-password/ (PUT)
- /api_auth/users/ (GET)

### Service Endpoints
- /api_services/blog/ (GET)
- /api_services/order/ (GET, POST)
- /api_services/order/{id}/ (GET, POST, DELETE)
- /api_services/service/ (GET)
- /api_services/service/{id}/ (GET)
- /api_services/sub-service/ (GET)
- /api_services/sub-service/{id}/ (GET)
- /api_services/service-choices/ (GET)
- /api_services/service-choices/{id}/ (GET)


### Tasker Endpoints
- /api_services/tasker/ (GET)
- /api_services/tasker/{id}/ (GET)


## Contributing

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch with your changes using the command `git checkout -b your-branch-name`.
3. Make your changes and commit them using the command `git commit -m "Your commit message"`.
4. Push your changes to your forked repository using the command `git push origin your-branch-name`.
5. Create a pull request to the original repository.



## Credits

- Django: https://www.djangoproject.com/
- Django Rest Framework: https://www.django-rest-framework.org/
- Postman: https://www.postman.com/
