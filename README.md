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

4. Run database migrations:

```
python manage.py migrate

```

5. Start the development server:

```
python manage.py runserver

```

6. Access the API documentation at http://localhost:8000/swagger/ or http://localhost:8000/redoc/.

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
