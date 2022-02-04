function deleteCart() {
  fetch({
    method: "POST",
    body: JSON.stringify({ cartId: cartId }),
  }).then((response) => {
    window.location.href = "/";
  });
}

function init() {
  let carts = document.getElementById("carts").children;

  for (let cart of carts) {
    cart.addEventListener("click", activate);
  }
}

console.log(carts);
function test() {
  console.log("asdf");
}

let activated;

function activate() {
  if (activated) {
    activated.setAttribute("class", "list-group-item list-group-item-action");

    let items = activated.querySelector(".items");

    items.setAttribute("class", "items d-none");
  }

  let items = this.querySelector(".items");
  items.setAttribute("class", "p-2 items");

  this.setAttribute("class", "list-group-item list-group-item-action active");
  activated = this;
}

function deleteCart(cartId) {
  cart = document.getElementById(cartId);

  cart.remove();
  fetch("/delete-cart", {
    method: "POST",
    body: JSON.stringify({ cartId: cartId }),
  });
}

function addItem() {
  
}

init();
