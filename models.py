from app import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(255))
    amount = db.Column(db.Float)
    payment_date = db.Column(db.Date)
    status = db.Column(db.String(255))
    due_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Payment(id={self.id}, " \
               f"company='{self.company}', " \
               f"amount={self.amount}, " \
               f"payment_date='{self.payment_date}', " \
               f"status='{self.status}', " \
               f"due_date='{self.due_date}')>"

