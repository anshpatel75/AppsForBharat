import { getUser, isAdmin, logout } from './auth.js';
import { fetchProducts } from './api.js';
import { renderProducts } from './ui.js';

document.addEventListener('DOMContentLoaded', async () => {
  const authBtn = document.getElementById('authBtn');
  const cartBtn = document.getElementById('cartBtn');

  if (getUser()) {
    authBtn.textContent = 'Logout';
    authBtn.addEventListener('click', logout);

    // Show cart button only for non-admins
    if (!isAdmin()) {
      cartBtn.style.display = 'inline-block';
      cartBtn.addEventListener('click', () => {
        window.location.href = 'cart.html';
      });
    }
  } else {
    authBtn.textContent = 'Login';
    authBtn.addEventListener('click', () => {
      window.location.href = 'login.html';
    });
  }

  try {
    const products = await fetchProducts();
    renderProducts(products);
  } catch (err) {
    alert(err.message);
  }
});




window.addToCart = function (id, name, description, price) {
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  const existing = cart.find(i => i.product_id === id);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ product_id: id, name, description, price, quantity: 1 });
  }
  localStorage.setItem('cart', JSON.stringify(cart));
  alert("Item added to cart!");
};
