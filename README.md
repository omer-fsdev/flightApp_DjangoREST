# FlightApp

FlightApp is a backend project developed using Django REST Framework. It provides an API for managing flights, passengers, and reservations.

## Requirements

- Python 3.9 or higher
- Django 4.2.1
- djangorestframework 3.14.0
- Other dependencies listed in requirements.txt

## Installation

1. Clone the repository:

```
git clone https://github.com/omer-fsdev/flightApp_DjangoREST.git
```

2. Create a virtual environment and activate it:

```
   python -m venv env
   source env/bin/activate  # Linux/Mac
   .\env\Scripts\activate  # Windows
```

3. Install the required packages:

```

pip install -r requirements.txt

```

4. Create a .env file in the project root directory and configure the environment variables:

   ```
   SECRET_KEY = your_django_secret_key_here
   ENV_NAME= dev or prod
   SQL_DATABASE = your_database_name
   SQL_USER = your_database_user
   SQL_PASSWORD = your_database_password
   SQL_HOST = your_database_host
   SQL_PORT = your_database_port
   ```

5. Run database migrations:

```
python manage.py migrate

```

6. Start the development server:

```
python manage.py runserver

```

7. Access the API documentation at http://localhost:8000/swagger/ or http://localhost:8000/redoc/.

## Running Tests

To run the tests for the Flight App, execute the following command:

```
python manage.py test

```

## Test Coverage

To generate a test coverage report, you can use a coverage measurement tool like coverage.py.

1. Install it:

```
pip install coverage

```

2. Run the tests with coverage:

```
coverage run manage.py test


```

3. Generate the coverage report:

```
coverage report

```

## Project Plan

The FlightApp project follows the following structure:

### Models

- Flight: Represents a flight with relevant details such as origin, destination, departure time, etc.
- Passenger: Represents a passenger with information like name, email, etc.
- Reservation: Represents a reservation made by a passenger for a specific flight.

### Functionality

Flight

- Clients (API consumers):
  - Can view upcoming flights.
- Staff users (API consumers with staff privileges):
  - Can view all flights along with reservations.
  - Can perform CRUD (Create, Read, Update, Delete) operations on flights.

Reservation

- Clients (API consumers):
  - Can perform CRUD operations on their own reservations.
- Staff users (API consumers with staff privileges):
  - Can perform CRUD operations on all reservations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License.
