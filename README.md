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



## Frontend Work

📱 Mobile Store – Frontend (HTML + CSS + JS)<br>
This is a frontend application for a simple e-commerce mobile store built using HTML, CSS, and Vanilla JavaScript, designed to work seamlessly with a FastAPI backend.

#### 🚀 Features
🛍️ Product listing page (index.html)<br>

🔐 User login with admin detection<br>

⚙️ Admin panel to add/edit/delete products<br>

🛒 Cart with localStorage support<br>

✅ Place order and view order history<br>

🔁 Login/logout toggle, auto session detection<br>

📦 Fully responsive, BEM-based CSS styling<br>


## Folder Structure 

frontend/
├── index.html          # Product catalog (public)
├── login.html          # Login page
├── admin.html          # Admin panel for product CRUD
├── cart.html           # Cart management page
├── orders.html         # Order history page
├── css/
│   └── styles.css      # Shared BEM-style CSS
├── js/
│   ├── api.js          # API functions for products/orders
│   ├── auth.js         # Login, logout, session utilities
│   ├── ui.js           # Render product grid
│   ├── events.js       # Main logic for index.html
│   ├── cart.js         # Logic for cart operations
│   └── order.js        # Logic for order history


## ⚙️ How It Works

## 🔐 Authentication
    - Users log in via login.html
    - Session (user_id and is_admin) is stored in localStorage
    - Admins are redirected to admin.html; others to index.html

## 🛍️ Product Catalog (index.html)
    - Loads all products using /products
    - Users can add items to cart using Add to Cart button
    - Header button shows Login or Logout dynamically

## 🧑‍💼 Admin Panel (admin.html)
    - Only accessible to admins
    - Admins can:
        - Add new product (POST /products)
        - Edit product (PUT /products/{id})
        - Delete product (DELETE /products/{id})

## 🛒 Cart (cart.html)
    - Uses localStorage to maintain cart items
    - Items are synced with backend using /cart/add
    - Order is placed using /orders/create

## 📦 Orders (orders.html)
    - Loads order history using /orders/history
    - Shows all past orders with items and status



#### Admin/User Test Credentials
These users are pre-registered in the backend:<br>
| Role  | Username   | Password    |
| ----- | ---------- | ----------- |
| Admin | `admin123` | `adminpass` |
| User  | `user123`  | `userpass`  |


#### 🧩 Integration
This frontend is built to work with the following FastAPI endpoints:

Endpoint	            Method	       Description

/register	            POST	       Register user
/login	                POST	       Authenticate user
/products	            GET	           List all products
/products	            POST	       Add new product
/products/{id}	        PUT	           Update product
/products/{id}	        DELETE	       Delete product
/cart/add	            POST	       Add item to user cart
/orders/create	        POST	       Place order from cart
/orders/history	        GET	           View user’s past orders

### 🧪 Testing
Open index.html directly in a browser
    - No build tools required (pure HTML/CSS/JS)
    - Test full flow: login → cart → order → admin panel (if admin)

## 📎 Dependencies
No frameworks or libraries are used. Pure:
    - HTML5
    - CSS3 (BEM methodology)
    - Vanilla JavaScript (ES6 modules)

## 🙌 Credits
    - Developed by Ansh Patel
    - Designed for integration with FastAPI backend assignment project.


