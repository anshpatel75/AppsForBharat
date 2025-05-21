# AppsForBharat

# 📱 E-Commerce Backend (FastAPI)

A backend system for an e-commerce website that sells mobile phones online. Built using **FastAPI**, this mock solution demonstrates core backend functionality using in-memory storage (no real database or payment gateway integration).

---

## 🚀 Features

- ✅ User registration and login
- 📦 Product listing and details (with pagination)
- 🛒 Cart management (add/view/remove items)
- 🧾 Order creation with mock payment
- 📜 Order history with pagination
- 🧱 Clean architecture principles (SOLID-friendly)
- 🧪 Ready for unit testing

---

## 🧰 Tech Stack

- **Language:** Python 3.8+
- **Framework:** FastAPI
- **Data Storage:** In-memory dictionaries (simulates DB)
- **Dependencies:** Uvicorn, Pydantic

---

## 📂 Project Structure
ecommerce/<br>
├── backend.py # Main FastAPI app with all endpoints<br>
├── README.md # Project documentation<br>
├── API.md #  API documentation with endpoints and sample JSON responses<br>


## Database Schema

1. Users<br>
user_id VARCHAR PRIMARY KEY,<br>
password_hash TEXT NOT NULL

2. Products<br>
product_id SERIAL PRIMARY KEY,<br>
name TEXT,<br>
description TEXT,<br>
price FLOAT,<br>
inventory INT

3. Cart
cart_id SERIAL PRIMARY KEY,<br>
user_id VARCHAR REFERENCES users(user_id)<br>

4. CartItems<br>
cart_id INT REFERENCES cart(cart_id),<br>
product_id INT REFERENCES products(product_id),<br>
quantity INT<br>


5. Orders <br>
order_id SERIAL PRIMARY KEY,<br>
user_id VARCHAR REFERENCES users(user_id),<br>
status TEXT DEFAULT 'Placed',<br>
timestamp TIMESTAMP

6. OrderItems <br>
order_id INT REFERENCES orders(order_id), <br>
product_id INT REFERENCES products(product_id), <br>
quantity INT <br>

## API Endpoints

Auth<br>
   - POST /register – user registration<br>
   - POST /login – returns token or session<br>

Product<br>
    - GET /products?page=1&limit=10 – paginated product listing<br>
    - GET /products/{id} – view single product<br>
    - POST /products – add product (admin-only)<br>
    - PUT /products/{id} – update product<br>
    - DELETE /products/{id} – delete product<br>

Cart<br>
    - POST /cart/add – add item to cart<br>
    - GET /cart – view cart<br>
    - DELETE /cart/remove/{product_id} – remove item<br>

Order<br>
    - POST /orders/create – creates an order from cart (mock payment)<br>
    - GET /orders/history?page=1&limit=5 – user's order history<br>





