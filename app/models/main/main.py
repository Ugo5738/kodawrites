from app.extensions import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    second_name = db.Column(db.String(150))
    email = db.Column(db.Text)
    payment_method = db.Column(db.Text)
    created = db.Column(db.String(150))

    def __repr__(self):
        return f"<{self.first_name} {self.second_name}>"


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float(150))
    created = db.Column(db.String(150))

    def __repr__(self):
        return f"{self.amount}>"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150))

    def __repr__(self):
        return f"{self.product_name}>"

