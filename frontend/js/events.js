import { fetchProducts } from './api.js';
import { renderProducts } from './ui.js';

document.addEventListener('DOMContentLoaded', async () => {
  try {
    const products = await fetchProducts();
    renderProducts(products);
  } catch (err) {
    alert(err.message);
  }

  document.getElementById('loginBtn')?.addEventListener('click', () => {
    window.location.href = 'login.html';
  });
});
