import { getUser, logout} from './auth.js';

document.getElementById('logoutBtn')?.addEventListener('click', logout);


let cart = JSON.parse(localStorage.getItem('cart')) || [];

function updateCartView() {
  const container = document.getElementById('cartList');
  const totalDisplay = document.getElementById('cartTotal');
  container.innerHTML = '';
  let total = 0;

  cart.forEach(item => {
    const div = document.createElement('div');
    div.className = 'product-card';
    div.innerHTML = `
      <h3 class="product-card__title">${item.name}</h3>
      <p class="product-card__description">${item.description}</p>
      <p class="product-card__price">$${item.price} x ${item.quantity}</p>
      <button class="admin__delete" data-id="${item.product_id}">Remove</button>
    `;
    container.appendChild(div);
    total += item.price * item.quantity;
  });

  totalDisplay.textContent = total.toFixed(2);

  document.querySelectorAll('.admin__delete').forEach(btn => {
    btn.addEventListener('click', e => {
      const id = e.target.dataset.id;
      cart = cart.filter(i => i.product_id !== id);
      localStorage.setItem('cart', JSON.stringify(cart));
      updateCartView();
    });
  });
}

document.getElementById('placeOrderBtn').addEventListener('click', async () => {
  const user_id = getUser();
  if (!user_id) {
    alert("Please login to place order.");
    window.location.href = 'login.html';
    return;
  }

  if (!cart.length) {
    alert("Cart is empty!");
    return;
  }

  try {
    // 1. Sync localStorage cart with backend cart
    for (let item of cart) {
      await fetch(`http://localhost:8000/cart/add?user_id=${user_id}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: item.product_id, quantity: item.quantity })
      });
    }

    // 2. Place order
    const res = await fetch(`http://localhost:8000/orders/create?user_id=${user_id}`, {
      method: 'POST'
    });

    if (!res.ok) throw new Error("Order creation failed");

    const data = await res.json();
    alert(`Order placed successfully! Order ID: ${data.order_id}`);

    cart = [];
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartView();

    setTimeout(() => {
      window.location.href = 'orders.html';
    }, 1000);
  } catch (err) {
    alert("Error: " + err.message);
  }
});


updateCartView();
