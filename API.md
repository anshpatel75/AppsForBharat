# 📄 API Endpoints & Responses

### 🧑‍💻 Auth APIs

#### `POST /register`

Registers a new user.

**Request**

```json
{
  "user_id": "john123",
  "password": "securepass"
}
```

**Success**

```json
{
  "message": "User registered successfully"
}
```

**Failure**

```json
{
  "detail": "User already exists"
}
```

---

#### `POST /login`

Logs in the user.

**Request**

```json
{
  "user_id": "john123",
  "password": "securepass"
}
```

**Success**

```json
{
  "message": "Login successful"
}
```

**Failure**

```json
{
  "detail": "Invalid credentials"
}
```

---

### 📦 Product APIs

#### `POST /products`

Adds a new product (admin-only).

**Request**

```json
{
  "product_id": "p001",
  "name": "iPhone 15",
  "description": "Latest Apple flagship",
  "price": 1299.99,
  "inventory": 10
}
```

**Success**

```json
{
  "message": "Product added"
}
```

---

#### `GET /products`

Returns a paginated list of products.

**Success**

```json
[
  {
    "product_id": "p001",
    "name": "iPhone 15",
    "description": "Latest Apple flagship",
    "price": 1299.99,
    "inventory": 10
  }
]
```

---

#### `GET /products/{product_id}`

Returns detail of a specific product.

**Success**

```json
{
  "product_id": "p001",
  "name": "iPhone 15",
  "description": "Latest Apple flagship",
  "price": 1299.99,
  "inventory": 10
}
```

**Failure**

```json
{
  "detail": "Product not found"
}
```
---
#### 🆕 PUT `/products/{product_id}`
Update a product's details.

```json
{
  "product_id": "p001",
  "name": "iPhone 15 Pro",
  "description": "Updated Apple flagship",
  "price": 1399.99,
  "inventory": 8
}
```

**Success
```json
{
  "message": "Product updated successfully"
}
```

**failure
```json
{
  "detail": "Product not found"
}
```
---
#### DELETE /products/{product_id}
Delete a product from the catalog.

**Success
```json
{
  "message": "Product deleted successfully"
}
```

**Failure
```json
{
  "detail": "Product not found"
}
```



### 🛒 Cart APIs

#### `POST /cart/add?user_id={user_id}`

Adds a product to the user's cart.

**Request**

```json
{
  "product_id": "p001",
  "quantity": 2
}
```

**Success**

```json
{
  "message": "Item added to cart"
}
```

---

#### `GET /cart?user_id={user_id}`

Returns all items in a user’s cart.

**Success**

```json
[
  {
    "product_id": "p001",
    "quantity": 2
  }
]
```

---

#### `DELETE /cart/remove/{product_id}?user_id={user_id}`

Removes a product from the cart.

**Success**

```json
{
  "message": "Item removed"
}
```

---

### 🧾 Order APIs

#### `POST /orders/create?user_id={user_id}`

Creates a new order for the given user's cart. Simulates payment.

**Success**

```json
{
  "order_id": "3f9c4aee-9a7c-4b63-bf1e-4a1085fd83f2",
  "status": "Placed",
  "payment": "Success"
}
```

**Failure**

```json
{
  "detail": "Cart is empty"
}
```

---

#### `GET /orders/history?user_id={user_id}`

Returns paginated order history for the user.

**Success**

```json
[
  {
    "order_id": "3f9c4aee-9a7c-4b63-bf1e-4a1085fd83f2",
    "user_id": "john123",
    "items": [
      {
        "product_id": "p001",
        "quantity": 2
      }
    ],
    "status": "Placed"
  }
]
```
