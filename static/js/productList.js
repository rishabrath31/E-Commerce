import { products } from "./product-list.js";

// DOM Elements
const productsContainer = document.querySelector(".products__container");

// Function to add products to DOM
function addProductsToDOM() {
  products.forEach((product) => addProduct(product));
}

// Function to add one single product
function addProduct(product) {
  const list_price = new Intl.NumberFormat("en-IN").format(
    product.price.list_price
  );
  const mrp = new Intl.NumberFormat("en-IN").format(product.price.mrp);
  const reviews = new Intl.NumberFormat("en-IN").format(product.reviews);
  let ratingMarkup = "";
  const emptyStars = 5 - product.rating;
  for (let i = 1; i <= product.rating; i++) {
    ratingMarkup += "<i class='fa-solid fa-star'></i>";
  }
  for (let j = 1; j <= emptyStars; j++) {
    ratingMarkup += "<i class='fa-regular fa-star'></i>";
  }
  const markup = `<div class="products__container-item">
  <img src="/static/${product.image_url}" alt="" />
  <div class="content">
    <a href="../Products/product${product.id}" class="title">
      ${product.title}
    </a>
    <div class="star_rating">
      ${ratingMarkup}
    </div>
    <span class="reviews">(${reviews} reviews)</span>
    <div class="price">
      <span class="list_price"><sup>₹</sup>${list_price}</span>
      <span class="mrp">₹${mrp}</span>
    </div>
  </div>
</div>`;
  productsContainer.innerHTML += markup;
}

window.onload = () => {
  addProductsToDOM();
};
