const payButton = document.querySelector("#stripe-button");

payButton.addEventListener('click', event => {
    fetch('/stripe-pay')
    .then((result) => {return result.json(); })
    .then((data) => {
        var stripe = Stripe(data.checkout_public_key);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({
            sessionId: data.checkout_session_id
        }).then((result) => {
            console.log("There is an error");
            console.log(result.error.message);
        });
    })
});