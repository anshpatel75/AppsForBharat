const BASE_URL = 'http://localhost:8000';

export async function fetchProducts() {
  const res = await fetch(`${BASE_URL}/products`);
  if (!res.ok) throw new Error('Failed to load products');
  return await res.json();
}

export async function login(user_id, password) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id, password })
  });
  if (!res.ok) throw new Error('Invalid login');
  return await res.json();
}

export async function addProduct(product) {
  const res = await fetch(`${BASE_URL}/products`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(product)
  });
  if (!res.ok) throw new Error('Failed to add product');
  return await res.json();
}

export async function deleteProduct(product_id) {
  const res = await fetch(`${BASE_URL}/products/${product_id}`, {
    method: 'DELETE'
  });
  if (!res.ok) throw new Error('Failed to delete product');
  return await res.json();
}


export async function updateProduct(product) {
  const res = await fetch(`http://localhost:8000/products/${product.product_id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(product)
  });

  if (!res.ok) {
    throw new Error('Failed to update product');
  }

  return await res.json();
}


