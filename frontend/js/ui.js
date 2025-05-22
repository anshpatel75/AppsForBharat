/*export function renderProducts(products) {
  const container = document.getElementById('productList');
  container.innerHTML = '';

  products.forEach(product => {
    const div = document.createElement('div');
    div.className = 'product-card';
    div.innerHTML = `
      <img src="${product.image || 'https://via.placeholder.com/250'}" alt="${product.name}" class="product-card__image" />
      <h2 class="product-card__title">${product.name}</h2>
      <p class="product-card__description">${product.description}</p>
      <p class="product-card__price">$${product.price}</p>
      <button class="admin__button" onclick="addToCart('${product.product_id}', '${product.name}', '${product.description}', ${product.price})">
        Add to Cart
      </button>
    `;
    container.appendChild(div);
  });
}*/

export function renderProducts(products) {
  const container = document.getElementById('productList');
  container.innerHTML = '';

  products.forEach(product => {
    const div = document.createElement('div');
    div.className = 'product-card';
    div.innerHTML = `
      <img src="${product.image || 'https://via.placeholder.com/250'}" alt="${product.name}" class="product-card__image" />
      <h2 class="product-card__title">${product.name}</h2>
      <p class="product-card__description">${product.description}</p>
      <p class="product-card__price">$${product.price}</p>
      <button class="admin__button" onclick="addToCart('${product.product_id}', '${product.name}', '${product.description}', ${product.price})">
        Add to Cart
      </button>
    `;
    container.appendChild(div);
  });
}


