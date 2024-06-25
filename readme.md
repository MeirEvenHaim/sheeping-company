# CRUD Backend with SQLAlchemy, Marshmallow, and Bcrypt

## Project Overview

This project is a backend-only implementation of a CRUD (Create, Read, Update, Delete) application using Flask, SQLAlchemy, Marshmallow, and Bcrypt. The application manages data for emails, login information, clients, houses/estates, and mortgages. The project will be tested using Thunder Client.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Database Models](#database-models)
5. [API Endpoints](#api-endpoints)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Future Improvements](#future-improvements)
9. [License](#license)

## Project Structure
├── app
│ ├── init.py
│ ├── models.py
│ ├── schemas.py
│ ├── routes.py
│ └── utils.py
├── migrations
│ └── ...
├── tests
│ └── ...
├── config.py
├── run.py
└── README.md



- `app/`: Contains the main application files.
  - `__init__.py`: Initializes the Flask application and database.
  - `models.py`: Defines the database models.
  - `schemas.py`: Defines the Marshmallow schemas for serialization/deserialization.
  - `routes.py`: Defines the API endpoints.
  - `utils.py`: Contains utility functions for the application.
- `migrations/`: Directory for database migrations.
- `tests/`: Directory for unit tests.
- `config.py`: Configuration file for the application.
- `run.py`: Entry point for running the Flask application.
- `README.md`: Documentation file.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/crud-backend.git
    cd crud-backend
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Configuration

Configure the application settings in `config.py`:

```python
import os

 class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

class Email(db.Model):
    id = db.Column(db.Integer, primary key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
class Client(db.Model):
    id = db.Column(db.Integer, primary key=True)
    name = db.Column(db.String(100), nullable=False)


class House(db.Model):
    id = db.Column(db.Integer, primary key=True)
    address = db.Column(db.String(200), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('houses', lazy=True))

class Mortgage(db.Model):
    id = db.Column(db.Integer, primary key=True)
    amount = db.Column(db.Float, nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    house = db.relationship('House', backref=db.backref('mortgages', lazy=True))





1. 
API Endpoints

Email Endpoints
GET /emails: Retrieve all emails.
POST /emails: Create a new email.
GET /emails/<id>: Retrieve a single email by ID.
PUT /emails/<id>: Update an email by ID.
DELETE /emails/<id>: Delete an email by ID.

User Endpoints
POST /register: Register a new user.
POST /login: Authenticate a user and return a token.

Client Endpoints
GET /clients: Retrieve all clients.
POST /clients: Create a new client.
GET /clients/<id>: Retrieve a single client by ID.
PUT /clients/<id>: Update a client by ID.
DELETE /clients/<id>: Delete a client by ID.

House Endpoints
GET /houses: Retrieve all houses.
POST /houses: Create a new house.
GET /houses/<id>: Retrieve a single house by ID.
PUT /houses/<id>: Update a house by ID.
DELETE /houses/<id>: Delete a house by ID.

Mortgage Endpoints
GET /mortgages: Retrieve all mortgages.
POST /mortgages: Create a new mortgage.
GET /mortgages/<id>: Retrieve a single mortgage by ID.
PUT /mortgages/<id>: Update a mortgage by ID.
DELETE /mortgages/<id>: Delete a mortgage by ID.
Usage
Run the Flask application:

flask run
Access the API: The API will be accessible at http://127.0.0.1:5000/.

Testing
Use Thunder Client to test the API endpoints:

Open Thunder Client in your VSCode editor.
Create a new request and configure it with the appropriate method (GET, POST, PUT, DELETE) and URL.
Set the request body (for POST and PUT requests) to the necessary JSON payload.
Send the request and check the response.
Example request for creating a new client:

Method: POST
URL: http://127.0.0.1:5000/clients
Body:
#json
{
    "name": "John Doe"
}



2. 
Testing
Use Thunder Client to test the API endpoints:

Open Thunder Client in your VSCode editor.
Create a new request and configure it with the appropriate method (GET, POST, PUT, DELETE) and URL.
Set the request body (for POST and PUT requests) to the necessary JSON payload.
Send the request and check the response.
Example request for creating a new client:

Method: POST
URL: http://127.0.0.1:5000/clients


Future Improvements
Add user authentication and authorization.
Implement unit tests for all endpoints.
Add more detailed validation and error handling.
Enhance the documentation with example requests and responses.