export function renderProducts(products) {
  const container = document.getElementById('productList');
  container.innerHTML = '';
  products.forEach(product => {
    const div = document.createElement('div');
    div.className = 'product-card';
    div.innerHTML = `
      <h2 class="product-card__title">${product.name}</h2>
      <p class="product-card__description">${product.description}</p>
      <p class="product-card__price">$${product.price}</p>
    `;
    container.appendChild(div);
  });
}
