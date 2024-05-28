# Mini Project: E-commerce API

# In today's digital age, online shopping has become an integral part of our lives. E-commerce platforms have revolutionized the way we purchase products, offering convenience, 
# variety, and accessibility like never before. However, building a robust e-commerce application from scratch can be a complex task, involving various components such as user 
# management, product listings, shopping carts, and order processing.

# Imagine you are tasked with creating an e-commerce application that empowers both customers and administrators. The goal is to build a user-friendly platform where customers 
# can effortlessly browse products, add them to their shopping carts, and place orders. Simultaneously, administrators should have tools to manage product inventory, track orders, 
# and ensure a seamless shopping experience.

# To tackle this challenge, we will leverage the power of Python and two essential libraries: Flask and Flask-SQLAlchemy. Flask is a lightweight web framework that simplifies 
# web application development, while Flask-SQLAlchemy provides a robust toolkit for database interactions. Together, they form the perfect duo to craft our e-commerce solution.

# In this project, we will guide you through the process of building an e-commerce application that closely mimics real-world scenarios.

# Project Requirements
# To successfully build our e-commerce application and achieve the learning objectives, we need to establish clear project requirements. These requirements outline the key features 
# and functionalities that our application must encompass. Below, you'll find a comprehensive list of project requirements based on our learning objectives:

# 1. Customer and CustomerAccount Management: Create the CRUD (Create, Read, Update, Delete) endpoints for managing Customers and their associated CustomerAccounts:
# - Create Customer: Implement an endpoint to add a new customer to the database. Ensure that you capture essential customer information, including name, email, and phone number.
# - Read Customer: Develop an endpoint to retrieve customer details based on their unique identifier (ID). Provide functionality to query and display customer information.
# - Update Customer: Create an endpoint for updating customer details, allowing modifications to the customer's name, email, and phone number.
# - Delete Customer: Implement an endpoint to delete a customer from the system based on their ID.
# - Create CustomerAccount: Develop an endpoint to create a new customer account. This should include fields for a unique username and a secure password.
# - Read CustomerAccount: Implement an endpoint to retrieve customer account details, including the associated customer's information.
# - Update CustomerAccount: Create an endpoint for updating customer account information, including the username and password.
# - Delete CustomerAccount: Develop an endpoint to delete a customer account.
# 2. Product Catalog: Create the CRUD (Create, Read, Update, Delete) endpoints for managing Products:
# - Create Product: Implement an endpoint to add a new product to the e-commerce database. Capture essential product details, such as the product name and price.
# - Read Product: Develop an endpoint to retrieve product details based on the product's unique identifier (ID). Provide functionality to query and display product information.
# - Update Product: Create an endpoint for updating product details, allowing modifications to the product name and price.
# - Delete Product: Implement an endpoint to delete a product from the system based on its unique ID.
# - List Products: Develop an endpoint to list all available products in the e-commerce platform. Ensure that the list provides essential product information.
# - View and Manage Product Stock Levels (Bonus): Create an endpoint that allows to view and manage the stock levels of each product in the catalog. Administrators should be able to 
#   see the current stock level and make adjustments as needed.
# - Restock Products When Low (Bonus): Develop an endpoint that monitors product stock levels and triggers restocking when they fall below a specified threshold. Ensure that stock 
#   replenishment is efficient and timely.
# 3. Order Processing: Develop comprehensive Orders Management functionality to efficiently handle customer orders, ensuring that customers can place, track, and manage their orders seamlessly.
# - Place Order: Create an endpoint for customers to place new orders providing essential order details. Each order should capture the order date and the associated customer.
# - Retrieve Order: Implement an endpoint that allows customers to retrieve details of a specific order based on its unique identifier (ID). Provide a clear overview of the order, 
#   including the order date and associated products.
# - Manage Order History (Bonus): Create an endpoint that allows customers to access their order history, listing all previous orders placed. Each order entry should provide 
#   comprehensive information, including the order date and associated products.
# - Cancel Order (Bonus): Implement an order cancellation feature, allowing customers to cancel an order if it hasn't been shipped or completed. Ensure that canceled orders are 
#   appropriately reflected in the system.
# - Calculate Order Total Price (Bonus): Include an endpoint that calculates the total price of items in a specific order, considering the prices of the products included in the order. 
#   This calculation should be specific to each customer and each order, providing accurate pricing information.
# 4. Database Integration:
# - Utilize Flask-SQLAlchemy to integrate a MySQL database into the application.
# - Design and create the necessary Model to represent customers, orders, products, customer accounts, and any additional features.
# - Establish relationships between tables to model the application's core functionality.
# - Ensure proper database connections and interactions for data storage and retrieval.
# 5. Error Handling:
# - (BONUS) Implement data validation mechanisms to ensure that user inputs meet specified criteria (e.g., valid email addresses, proper formatting).
# - Use try, except, else, and finally blocks to handle errors gracefully and provide informative error messages to guide users.
# 6. User Interface (Postman):
# - Develop Postman collections that categorize and group API requests according to their functionality. Separate collections for Customer Management, Product Management, Order Management, 
#   and Bonus Features should be created for clarity.
# 7. GitHub Repository:
# - Create a GitHub repository for the project and commit code regularly.
# - Maintain a clean and interactive README.md file in the GitHub repository, providing clear instructions on how to run the application and explanations of its features.
# - Include a link to the GitHub repository in the project documentation.

# Project Tips
# Building an e-commerce application can be both exciting and challenging. To help you navigate this journey successfully and achieve the project requirements, here are some valuable 
# tips to keep in mind:
# 1. Plan Your Database Structure:
# - Model Design: Carefully design your database models to accurately represent customers, orders, products, customer accounts, and any additional features you plan to incorporate. 
#   Ensure that you establish the necessary relationships between tables to model your application's core functionality effectively.
# 2. Data Validation and Error Handling:
# - (BONUS) Data Validation: Implement robust data validation mechanisms to ensure that user inputs meet specified criteria. This is crucial for maintaining data integrity and 
#   preventing issues down the line.
# - Error Handling: Utilize try, except, else, and finally blocks to handle errors gracefully. Provide informative error messages that guide users in troubleshooting and resolving issues.
# 3. Thorough Testing with Postman:
# - Postman Collections: Create organized Postman collections that categorize and group API requests based on functionality. This will make it easier to test and validate different 
#   parts of your application.
# - Documentation: Include clear documentation within your Postman collections and requests. This documentation should guide users on how to use each request effectively. Comments 
#   and descriptions should be concise and informative.
# 4. GitHub Repository and Version Control:
# Repository Management: Establish a GitHub repository for your project and commit code regularly. Utilize version control to keep track of changes and collaborate effectively with 
# team members if applicable.
# README.md: Maintain a clean and interactive README.md file in your GitHub repository. Provide clear instructions on how to run the application and explanations of its features. 
# Include a link to your GitHub repository in your project documentation.
# 5. Effective Communication:
# Remember that building a robust e-commerce application is a process that involves careful planning, coding, testing, and documentation. By following these project tips and adhering 
# to the requirements, you'll be well on your way to creating a successful and feature-rich e-commerce platform. Good luck with your project!

# Conclusion
# Our e-commerce project presents an exciting opportunity to apply the knowledge and skills gained throughout our learning journey. By following the project requirements and tips provided,
# we can develop a robust and feature-rich e-commerce application.

# We've emphasized the importance of code reusability, efficient database design, data validation, and thorough testing using Postman. Additionally, maintaining a well-documented GitHub 
# repository and effectively communicating project details demonstrate our commitment to producing a high-quality solution.

# As we embark on this project, we're not only building an e-commerce application but also gaining practical experience in software development, database integration, and API design. 
# This project serves as a significant step toward becoming proficient developers and showcases our ability to tackle real-world challenges.

# By following these guidelines and giving our best effort, we're well-prepared to create an impressive e-commerce platform that meets the project's objectives and showcases our skills 
# as developers. So, let's dive in and make this e-commerce project a success!


from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate, ValidationError
from typing import List
import datetime
import re

app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:your_password@localhost/online_shopping"
app.json.sort_keys = False

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)

class Customer(Base):
    __tablename__ = "Customers"
    customer_id: Mapped[int] = mapped_column(autoincrement=True, primary_key = True)
    name: Mapped[str] = mapped_column(db.String(255))
    email: Mapped[str] = mapped_column(db.String(320))
    phone: Mapped[str] = mapped_column(db.String(15))
    # One-to-one relationship:
    customer_account: Mapped["CustomerAccount"] = db.relationship(back_populates="customer")
    # Tying the customer_account attribute to the CustomerAccount class
    # Allowing us to see CustomerAccount info through the customer object
    # Creating the one-to-many relationship with the orders table:
    orders: Mapped[List["Order"]] = db.relationship(back_populates="customer")
    # orders is a list of Order objects

class CustomerAccount(Base):
    __tablename__ = "Customer_Accounts"
    account_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey("Customers.customer_id"))
    # One-to-one relationship between customer and customer_account
    customer: Mapped['Customer'] = db.relationship(back_populates="customer_account")

# Association table Order_Product for orders and products because 
# There is a many to many relationship
order_product = db.Table(
    "Order_Product",
    Base.metadata,
    db.Column("order_id", db.ForeignKey("Orders.order_id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("Products.product_id"), primary_key=True)
)

class Order(Base):
    __tablename__ = "Orders"
    order_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('Customers.customer_id'))
    status: Mapped[str] = mapped_column(db.String(50), nullable=False, default='pending')  # Adding status field for the bonus feature to work properly
    # Many-to-one relationship with the customer table
    customer: Mapped["Customer"] = db.relationship(back_populates="orders")
    products: Mapped[List["Product"]] = db.relationship(secondary=order_product, back_populates="orders")

class Product(Base):
    __tablename__ = "Products"
    product_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    stock_level: Mapped[int] = mapped_column(db.Integer, nullable=False, default=0)  # Adding stock_level field, the default value is set to 0
    orders: Mapped[List["Order"]] = db.relationship(secondary=order_product, back_populates="products")


with app.app_context():
    db.create_all()

# ============ CUSTOMER MANAGEMENT ============

class CustomerSchema(ma.Schema):
    customer_id = fields.Integer(required=False)
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ("customer_id", "name", "email", "phone")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

# Defining regex patterns to validate inputs:
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # Valid emails: example@example.com, user.name+tag@sub.domain.com
phone_regex = r'^\+?[1-9]\d{1,14}$' # Valid phone numbers: +12345678901234, 1234567890

# ====== API ROUTES ======

@app.route("/")
def home():
    return "Welcome to E-Commerce API!"


@app.route("/customers", methods = ["GET"])
def get_customers():
    # Using the class Customer as a model for the Customers table:
    query = select(Customer) # Creating a SELECT query for the customer table SELECT * FROM Customers
    result = db.session.execute(query).scalars() # Retrieving a ScalarResult, a generator-like object (rather than a list of rows or tuples), that can be iterated over to access each scalar value one at a time
    customers = result.all() # Fetching all rows of data from the result

    # Converting customers through the marshmallow schema and returning the response:
    return customers_schema.jsonify(customers)


@app.route("/customers/by-name", methods=["GET"])
def get_customer_by_name():
    name = request.args.get("name")
    search = f"%{name}%" # % is a wildcard
    # Using % with LIKE to find partial matches:
    query = select(Customer).where(Customer.name.like(search)).order_by(Customer.name.asc())

    customers = db.session.execute(query).scalars().all()

    return customers_schema.jsonify(customers)


@app.route("/customers", methods=["POST"])
def add_customer():
    try:
        # Validating that the incoming data matches our schema:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Validating the customer_data (email and phone number):
    if not re.match(email_regex, customer_data['email']):
        return jsonify({"error": "Invalid email format"}), 400
    if not re.match(phone_regex, customer_data['phone']):
        return jsonify({"error": "Invalid phone number format"}), 400
    
    with Session(db.engine) as session: # Creating a session object, allowing us to make changes to our database
        with session.begin(): # Creating a transaction to interact with the database
            name = customer_data['name']
            email = customer_data['email']
            phone = customer_data['phone']
            # Using information from the request to instantiate our Customer class
            new_customer = Customer(name=name, email=email, phone=phone)
            # Adding the new_customer object to the database
            session.add(new_customer)
            session.commit()  # Saving changes to our database
    return jsonify({"message": "New customer added successfully"}), 201 # New resource has been created on the server


@app.route('/customers/<int:customer_id>', methods=["PUT"])
def updated_customer(customer_id):
    with Session(db.engine) as session: # Creating a session object using the SQLAlchemy Engine
        with session.begin(): # Starting the transaction :  
            # Retrieving a customer with the customer_id passed in from the request:
                            #class      #class, not table
            query = select(Customer).filter(Customer.customer_id == customer_id)
            result = session.execute(query).scalars().first() # Returning query results as an object and grabbing the first record returned
            if result is None:
                return jsonify({"error": "Customer not found"}), 404
            
            customer = result # Naming the customer variable that we're working with

            try:
                customer_data = customer_schema.load(request.json)
                # Put regex here to validate the email that's coming to the database, also do the except
            except ValidationError as err:
                return jsonify(err.messages), 400
            
            if 'email' in customer_data and not re.match(email_regex, customer_data['email']):
                return jsonify({"error": "Invalid email format"}), 400
            if 'phone' in customer_data and not re.match(phone_regex, customer_data['phone']):
                return jsonify({"error": "Invalid phone number format"}), 400

            # Updating the customer attributes:
            for field, value in customer_data.items():
                setattr(customer, field, value)

            session.commit()
            return jsonify({"message": "Customer details successfully updated"}), 200


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    # Delete statement where we delete from the customer table where customer_id is a parameter
    # Matching an id within the database
    delete_statement = delete(Customer).where(Customer.customer_id==customer_id)
    with db.session.begin():
        result = db.session.execute(delete_statement) # Executing the delete statement

        # Checking if the customer existed to delete:
        if result.rowcount==0: # Checking that no rows were returned from the delete_statement execution. Same as "If result is None"
            return jsonify({"error": "Customer not found"}), 404
        
        return jsonify({"message": "Customer removed successfully!"})
      

# ============ PRODUCT MANAGEMENT ============

class ProductSchema(ma.Schema):
    product_id = fields.Integer(required=False)
    name = fields.String(required=True, validate=validate.Length(min=1)) # At least, one character is needed
    price = fields.Float(required=True, validate=validate.Range(min=0)) # No min, if free, we'll show at least 0
    stock_level = fields.Integer(required=True, validate=validate.Range(min=0)) # The stock level must be at least zero to create or update the product

    class Meta:
        fields = ("product_id", "name", "price", "stock_level")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# ====== API ROUTES ======

@app.route('/products', methods=["POST"])
def add_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    with Session(db.engine) as session:
        with session.begin():
            # new_product = Product(**product_data) # This unpacks our product data or we can use traditional method (either is fine):
            new_product = Product(name=product_data['name'], price=product_data['price'], stock_level=product_data['stock_level'])
            session.add(new_product)
            session.commit()

    return jsonify({"Message": "New product successfully added!"}), 201

@app.route('/products', methods=["GET"])
def get_products():
    query = select(Product) # SELECT * FROM Product in mySQL
    result = db.session.execute(query).scalars()
    products = result.all()

    return products_schema.jsonify(products)


@app.route("/products/by-name", methods=["GET"])
def get_product_by_name():
    name = request.args.get("name")
    search = f"%{name}%"
    query = select(Product).where(Product.name.like(search)).order_by(Product.price.asc())

    products = db.session.execute(query).scalars().all()

    return products_schema.jsonify(products)


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    with Session(db.engine) as session:
        with session.begin():
            query = select(Product).filter(Product.product_id == product_id)
            result = session.execute(query).scalar()
            # print(result)            
            
            if result is None:
                return jsonify({"error": "Product not found!"}), 404
            product = result
            try:
                product_data = product_schema.load(request.json)
            except ValidationError as err:
                return jsonify(err.messages), 400
            
            for field, value in product_data.items():
                setattr(product, field, value)

            session.commit()
            return jsonify({"message": "Product details successfully updated!"}), 200  


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    try:
        delete_statement = delete(Product).where(Product.product_id==product_id)
        with db.session.begin():
            result = db.session.execute(delete_statement)
            if result.rowcount == 0:
                return jsonify({"error": "Product not found"}), 404
            
            return jsonify({"message": "Product successfully deleted!"}), 200
    except IntegrityError:
        return jsonify({"error": "Cannot delete product because it is part of one or more orders."}), 400
    
# ==== BONUS ====

@app.route("/products/restock", methods=["POST"])
def restock_products():
    low_level = request.json.get('low_level', 5)
    restock_amount = request.json.get('restock_amount', 20)
    
    try:
        products_to_restock = db.session.execute(
            select(Product).where(Product.stock_level < low_level)
        ).scalars().all()
        
        if not products_to_restock:
            return jsonify({"message": "No products need restocking"}), 200
        
        for product in products_to_restock:
            product.stock_level += restock_amount
        
        db.session.commit()
        return jsonify({"message": "Products restocked successfully"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Although we can view and manage our stock_level using the endpoints above, here are separate endpoints that administrators can use just for these purposes.
# With proper authentication and authorization only administrators will have access to stock management endpoints.

@app.route("/products/<int:product_id>/stock", methods=["GET"])
def get_product_stock(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"product_id": product.product_id, "stock_level": product.stock_level}), 200


@app.route("/products/<int:product_id>/stock", methods=["PUT"])
def update_product_stock(product_id):
    try:
        product = db.session.get(Product, product_id)
        if product is None:
            return jsonify({"error": "Product not found"}), 404
        
        new_stock_level = request.json.get('stock_level')
        if new_stock_level is None or not isinstance(new_stock_level, int):
            return jsonify({"error": "Invalid stock level"}), 400
        
        product.stock_level = new_stock_level
        db.session.commit()
        return jsonify({"message": "Stock level updated successfully"}), 200
    except Exception as e:
        db.session.rollback() # rollback() will discard all modifications made during the transaction if the error occurs
        return jsonify({"error": str(e)}), 500
    

# ============ORDER MANAGEMENT============

class OrderSchema(ma.Schema):
    order_id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    date = fields.Date(required=True)
    status = fields.String(required=False, validate=validate.OneOf(['pending', 'shipped', 'completed', 'canceled']))  # Including status field for bonus feature to work properly
    product_ids = fields.List(fields.Integer(), required=True, load_only=True) # load_only=True specifies that  the field should only be used when deserializing (loading) data, not when serializing (dumping) it.
    products = fields.List(fields.Nested(lambda: ProductSchema(only=("product_id",))), dump_only=True) # dump_only=True means this field will only be included in the serialized output, not in the deserialized input.
    # lambda: ProductSchema(only=("product_id",)) is a way to specify that each product in the list should only include the product_id field when serialized

    class Meta:
        fields = ("order_id", "customer_id", "date", "status", "product_ids", "products")


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# ====== API ROUTES ======

@app.route("/orders", methods = ["POST"])
def add_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(customer_id=order_data['customer_id'], date=order_data['date'])  

            for product_id in order_data['product_ids']:
                product = session.get(Product, product_id)
                if product is None:
                    return jsonify({"error": f"Product with ID {product_id} not found"}), 404
                new_order.products.append(product)
            session.add(new_order)            
            session.commit()                  

    return jsonify({"message": "New order successfully added!"}), 201


@app.route("/orders", methods=["GET"])
def get_orders():
    query = select(Order)
    result = db.session.execute(query).scalars() # Fetching all rows of the result set as a list of scalar values, not tuples
    return orders_schema.jsonify(result)


@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = db.session.get(Order, order_id) # Retrieving an instance of the Order class from the database with the primary key order_id
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return order_schema.jsonify(order)


@app.route('/orders/<int:order_id>', methods=["PUT"])
def update_order(order_id):
    with Session(db.engine) as session:
        with session.begin():
            query = select(Order).filter(Order.order_id==order_id)
            result = session.execute(query).scalar()
            if result is None:
                return jsonify({"message": "Product Not Found"}), 404
            order = result
            try:
                order_data = order_schema.load(request.json)
            except ValidationError as err:
                return jsonify(err.messages), 400
            
            for field, value in order_data.items():
                setattr(order, field, value)

            session.commit()
            return jsonify({"Message": "Order was successfully updated!"}), 200
        

@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    try:
        delete_statement = delete(Order).where(Order.order_id==order_id)
        with db.session.begin():
            result = db.session.execute(delete_statement)
            if result.rowcount == 0:
                return jsonify({"error": "Order not found"}), 404
            return jsonify({"message": "Order removed successfully"}), 200
    except IntegrityError:
        return jsonify({"error": "Cannot delete order because it contains one or more products."}), 400
    
# ==== BONUS ====

@app.route("/customers/<int:customer_id>/orders", methods=["GET"])
def get_order_history(customer_id):
    orders = db.session.execute(
        select(Order).where(Order.customer_id == customer_id)).scalars().all()
    
    if not orders:
        return jsonify({"message": "No orders found for this customer"}), 404
    
    return orders_schema.jsonify(orders), 200


@app.route("/orders/<int:order_id>/cancel", methods=["PUT"])
def cancel_order(order_id):
    try:
        order = db.session.get(Order, order_id)
        if order is None:
            return jsonify({"error": "Order not found"}), 404
        
        # Checking if the order can be canceled:
        if order.status in ['shipped', 'completed']:
            return jsonify({"error": "Order cannot be canceled"}), 400
        
        # Updating the status to canceled:
        order.status = 'canceled'
        db.session.commit()
        
        return jsonify({"message": "Order canceled successfully"}), 200
    
    except Exception as e:
        db.session.rollback() # rollback() will discard all modifications made during the transaction if the error occurs or the changes need to be reverted
        return jsonify({"error": str(e)}), 500


@app.route("/orders/<int:order_id>/total", methods=["GET"])
def calculate_order_total(order_id):
    order = db.session.get(Order, order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    
    total_price = sum(product.price for product in order.products)
    
    return jsonify({"order_id": order.order_id, "total_price": total_price}), 200


# ============ CUSTOMER ACCOUNT MANAGEMENT ============

class CustomerAccountSchema(ma.Schema):
    account_id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    username = fields.String(required=True, validate=validate.Length(min=6))
    password = fields.String(required=True, validate=validate.Length(min=8))

    class Meta:
        fields = ("account_id", "customer_id", "username", "password")

customer_account_schema = CustomerAccountSchema()
customer_accounts_schema = CustomerAccountSchema(many=True)

# Defining regex patterns to validate inputs:
username_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$' # Valid username: user123 (at least one letter and one number, minimum 6)
password_regex = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%&?!+_-])[A-Za-z\d@#$%&?!+_-]{8,}$' # Valid passwords: Password1@, P@55w0rd!, 1234!Abcd (at least one letter, one number, and one special character, minimum 8)

# ====== API ROUTES ======

@app.route("/accounts", methods=["POST"])
def add_customer_account():
    try:
        customer_account_data = customer_account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Validating the customer_account_data (username and password):
    if not re.match(username_regex, customer_account_data['username']):
        return jsonify({"error": "Invalid username format"}), 400
    if not re.match(password_regex, customer_account_data['password']):
        return jsonify({"error": "Invalid password format"}), 400
    
    with Session(db.engine) as session:
        with session.begin():
            new_customer_account = CustomerAccount(customer_id=customer_account_data['customer_id'], username=customer_account_data['username'], password=customer_account_data['password'])
            session.add(new_customer_account)
            session.commit()
    return jsonify({"message": "New customer account added successfully"}), 201


@app.route("/accounts", methods = ["GET"])
def get_customer_accounts():
    query = select(CustomerAccount)
    result = db.session.execute(query).scalars()
    customer_accounts = result.all()

    return customer_accounts_schema.jsonify(customer_accounts)


@app.route('/accounts/<int:account_id>', methods=["PUT"])
def updated_customer_account(account_id):
    with Session(db.engine) as session:
        with session.begin():
            query = select(CustomerAccount).filter(CustomerAccount.account_id == account_id)
            result = session.execute(query).scalars().first()
            if result is None:
                return jsonify({"error": "Account not found"}), 404
            
            customer_account = result

            try:
                customer_account_data = customer_account_schema.load(request.json)
            except ValidationError as err:
                return jsonify(err.messages), 400
            
            if 'username' in customer_account_data and not re.match(username_regex, customer_account_data['username']):
                return jsonify({"error": "Invalid username format"}), 400
            if 'password' in customer_account_data and not re.match(password_regex, customer_account_data['password']):
                return jsonify({"error": "Invalid password format"}), 400

            for field, value in customer_account_data.items():
                setattr(customer_account, field, value)

            session.commit()
            return jsonify({"message": "Customer account details successfully updated"}), 200
        

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_customer_account(account_id):

    delete_statement = delete(CustomerAccount).where(CustomerAccount.account_id==account_id)

    with db.session.begin():
        result = db.session.execute(delete_statement)
        if result.rowcount == 0:
            return jsonify({"error": "Customer account not found" }), 404
        
        return jsonify({"message": "Customer account removed successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)