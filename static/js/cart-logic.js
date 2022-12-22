import cartItems from "./cart.js";

// Function to fetch cartItems
function getCartItems() {
  const items = cartItems.reduce((currTotal, item) => {
    return currTotal + item.quantity;
  }, 0);
  return items;
}

// DOM Elements
const numberOfItems = document.getElementById("numberOfItems");

// Set the total number of cart items
(function setCartItems() {
  numberOfItems.innerText = getCartItems();
})();
