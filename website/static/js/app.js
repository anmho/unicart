function init() {
  let carts = document.getElementById("carts").children;

  for (let cart of carts) {
    cart.addEventListener("click", highlightCart);
  }
}

let activated;

function highlightCart() {
  let items = this.querySelector(".items");

  if (activated == undefined) {
    // No Items selected
    items.setAttribute("class", "p-2 items");

    this.setAttribute("class", "list-group-item list-group-item-action active");
    activated = this;
  } else if (this == activated) {
    // This is already selected -> turn it off
    // Deactivate activated
    activated.setAttribute("class", "list-group-item list-group-item-action");
    // Hide items
    items.setAttribute("class", "items d-none");

    activated = undefined;
  } else {
    // Activate this
    this.setAttribute("class", "list-group-item list-group-item-action active");
    // Unhide items
    items.setAttribute("class", "p-2 items");

    // Deactivate activated
    activated.setAttribute("class", "list-group-item list-group-item-action");
    // Hide items
    let activatedItems = activated.querySelector(".items");
    activatedItems.setAttribute("class", "items d-none");

    activated = this;
  }
}

function deleteCart(cartId) {
  cart = document.getElementById(cartId);

  cart.remove();
  fetch("/delete-cart", {
    method: "POST",
    body: JSON.stringify({ cartId: cartId }),
  });
}

// function deleteCart() {
//   fetch({
//     method: "POST",
//     body: JSON.stringify({ cartId: cartId }),
//   }).then((response) => {
//     window.location.href = "/";
//   });
// }

// function toggleEditBtn() {
//   this.parentNode

// }

// function editItem(itemId) {
//   document.querySelector()
// }

function deleteItem(cartId, itemId) {
  let item = document.getElementById(itemId);

  item.remove();
  fetch("/delete-item", {
    method: "POST",
    body: JSON.stringify({
      cartId: cartId,
      itemId: itemId,
    }),
  });
}

init();
