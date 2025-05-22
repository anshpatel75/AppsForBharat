export function renderProducts(products) {
  const container = document.getElementById('productList');
  container.innerHTML = '';

  products.forEach(product => {
    const div = document.createElement('div');
    div.className = 'product-card';  // 🔥 Important class
    div.innerHTML = `
      <h3 class="product-card__title">${product.name}</h3>
      <p class="product-card__description">${product.description}</p>
      <p class="product-card__price">$${product.price}</p>
      <button class="admin__button" onclick="addToCart('${product.product_id}', '${product.name}', '${product.description}', ${product.price})">
        Add to Cart
      </button>
    `;
    container.appendChild(div);
  });
}



