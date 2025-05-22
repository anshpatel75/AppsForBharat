import { getUser, logout } from './auth.js';
document.getElementById('logoutBtn')?.addEventListener('click', logout);

async function loadOrders() {
  const user_id = getUser();
  if (!user_id) {
    alert("Login required to view orders.");
    window.location.href = 'login.html';
    return;
  }

  const res = await fetch(`http://localhost:8000/orders/history?user_id=${user_id}`);
  const orders = await res.json();
  const container = document.getElementById('orderList');

  if (!orders.length) {
    container.innerHTML = "<p>No orders found.</p>";
    return;
  }

  orders.forEach(order => {
    const div = document.createElement('div');
    div.className = 'product-card';
    const itemsHtml = order.items.map(i => `<li>${i.product_id} x ${i.quantity}</li>`).join("");
    div.innerHTML = `
      <h3 class="product-card__title">Order #${order.order_id}</h3>
      <ul class="order__items">${itemsHtml}</ul>
      <p>Status: <strong>${order.status}</strong></p>
    `;
    container.appendChild(div);
  });
}

loadOrders();
