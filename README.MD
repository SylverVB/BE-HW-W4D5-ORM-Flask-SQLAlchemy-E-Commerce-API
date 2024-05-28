# E-commerce API

This project is an E-commerce API built using Flask, Flask-SQLAlchemy, and Marshmallow. It provides endpoints for managing products, orders, and customer accounts. The API allows customers to browse products, add them to their shopping carts, place orders, and manage their accounts. Administrators can manage product inventory, track orders, and ensure a seamless shopping experience.

## Project Structure

The project consists of the following key files:

- `e_commerce_api_orm.py`: The main application file containing the Flask routes and logic for managing products, orders, and customer accounts.
- `online_shopping.sql`: The SQL script for setting up the database and altering tables.
- `requirements.txt`: A list of Python dependencies required for the project.

## Setup and Installation

### Prerequisites

- Python 3.7+
- MySQL server

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SylverVB/BE-HW-W4D5-ORM-Flask-SQLAlchemy-E-Commerce-API.git
   cd e-commerce-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the MySQL database:**

   - Start your MySQL server.
   - Run the SQL script to create the database and alter tables:
     ```bash
     mysql -u your_username -p < online_shopping.sql
     ```

5. **Configure the database connection:**
   
   Update the `e_commerce_api_orm.py` file to include your MySQL database credentials:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://your_username:your_password@localhost/online_shopping'
   ```

6. **Run the application:**
   ```bash
   flask run
   ```

## API Endpoints

### Customer Management

- **Get all customers**
  - `GET /customers`
  
- **Get customers by name**
  - `GET /customers/by-name?name=CustomerName`

- **Add a customer**
  - `POST /customers`
  - Request body: `{ "name": "Customer Name", "email": "email@example.com", "phone": "+1234567890" }`

- **Update a customer**
  - `PUT /customers/<int:customer_id>`
  - Request body: `{ "name": "Updated Name", "email": "updated_email@example.com", "phone": "+1234567890" }`

- **Delete a customer**
  - `DELETE /customers/<int:customer_id>`

### Product Management

- **Add a product**
  - `POST /products`
  - Request body: `{ "name": "Product Name", "price": 100.0, "stock_level": 10 }`

- **Get all products**
  - `GET /products`

- **Get products by name**
  - `GET /products/by-name?name=Product`

- **Update a product**
  - `PUT /products/<int:product_id>`
  - Request body: `{ "name": "Updated Name", "price": 150.0, "stock_level": 20 }`

- **Delete a product**
  - `DELETE /products/<int:product_id>`

### Order Management

- **Add an order**
  - `POST /orders`
  - Request body: `{ "customer_id": 1, "date": "2024-01-01", "product_ids": [1, 2, 3] }`

- **Get all orders**
  - `GET /orders`

- **Get an order by ID**
  - `GET /orders/<int:order_id>`

- **Update an order**
  - `PUT /orders/<int:order_id>`
  - Request body: `{ "customer_id": 1, "date": "2024-01-01", "status": "shipped", "product_ids": [1, 2] }`

- **Delete an order**
  - `DELETE /orders/<int:order_id>`

- **Get order history for a customer**
  - `GET /customers/<int:customer_id>/orders`

- **Cancel an order**
  - `PUT /orders/<int:order_id>/cancel`

- **Calculate order total**
  - `GET /orders/<int:order_id>/total`

### Customer Account Management

- **Add a customer account**
  - `POST /accounts`
  - Request body: `{ "customer_id": 1, "username": "user123", "password": "Password1@" }`

- **Get all customer accounts**
  - `GET /accounts`

- **Update a customer account**
  - `PUT /accounts/<int:account_id>`
  - Request body: `{ "username": "newuser123", "password": "NewPassword1@" }`

- **Delete a customer account**
  - `DELETE /accounts/<int:account_id>`

## Validation

- **Customer Validation:**
  - `name`: Required.
  - `email`: Required, must match the pattern `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`.
  - `phone`: Required, must match the pattern `^\+?[1-9]\d{1,14}$`.

- **Product Validation:**
  - `name`: Required.
  - `price`: Required, minimum 0.
  - `stock_level`: Required, minimum 0.

- **Order Validation:**
  - `customer_id`: Required.
  - `date`: Required.
  - `status`: Optional, must be one of `['pending', 'shipped', 'completed', 'canceled']`.
  - `product_ids`: Required, list of product IDs.

- **Customer Account Validation:**
  - `username`: Required, minimum 6 characters, must contain at least one letter and one number.
  - `password`: Required, minimum 8 characters, must contain at least one letter, one number, and one special character.

## Running the Tests

To run the tests, you can use the built-in Flask testing tools or any other testing framework of your choice. Ensure that you have a separate testing database to avoid conflicts with the production data.

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License:
This application is the property of Victor Bondaruk. However, it is unlicensed, which means that no specific license has been applied to it. As the owner, Victor Bondaruk retains all rights to the application.

## Contact:
For any inquiries or support, please contact Victor Bondaruk at user@example.com.