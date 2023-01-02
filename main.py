import os
from app import create_app
from app.utils import stripe_keys

import stripe


app = create_app()


stripe.api_key = stripe_keys["secret_key"]


if __name__ == '__main__':
    app.run()