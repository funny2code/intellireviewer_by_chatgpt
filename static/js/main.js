console.log("Sanity check!");
  
function validateForm() {
    // Validate the required fields
    var goals = document.getElementById("goals").value;
    var obstacles = document.getElementById("obstacles").value;
    var skills = document.getElementById("skills").value;

    if (goals === "" || obstacles === "" || skills === "") {
      alert("Please fill out all the required fields.");
      return false; // Prevent form submission
    }

    return true; // Allow form submission
}

// new
// Get Stripe publishable key
fetch("/config")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  // new
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/create-checkout-session")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});