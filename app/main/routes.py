from flask import request, render_template, url_for, abort
from app.main import bp

import stripe
from app.utils import stripe_keys


stripe.api_key = stripe_keys["secret_key"]


@bp.route('/')
def index():
    return render_template('index.html')


# PAYMENTS
@bp.route("/stripe-pay", methods=["GET", "POST"])
def stripe_pay():
    # product = stripe.Product.create(
    #     name='T-shirt',
    #     description='Comfortable cotton t-shirt',
    #     images=['https://example.com/t-shirt.png'],
    # )

    # price = stripe.Price.create(
    #     product=product.id,
    #     unit_amount=2000,
    #     currency='usd',
    # )

    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items = [
            {
                # "price": price.id,
                "price": "price_1MLWaOA1cs68GwAoDWqQaokM",
                "quantity": 1,
            }
        ],
        mode = "subscription", # payment
        success_url = url_for('main.success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url = url_for('main.cancel', _external=True),
    )

    return {
        "checkout_session_id": checkout_session['id'], 
        "checkout_public_key": stripe_keys["publishable_key"]
    }
    

@bp.route("/success")
def success():
    return render_template('payment/success.html')


@bp.route("/cancel")
def cancel():
    return render_template('payment/cancel.html')


@bp.route("/stripe-webhook", methods=["POST"])
def stripe_webhook():
    if request.content_length > 1024 * 1024:
        print("REQUEST TOO BIG")
        abort(400)

    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = stripe_keys["endpoint_secret"]
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        
        # TODO: run some custom code here
        checkout_session = event['data']['object']
        line_items = stripe.checkout.Session.list_line_items(checkout_session['id'], limit=1)
        print(line_items['data'][0]['description'])
    return "Success", 200