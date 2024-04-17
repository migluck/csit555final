from app.config.database import db
from datetime import datetime


class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company = db.Column(db.String(255))
    amount = db.Column(db.Float)
    payment_date = db.Column(db.Date)
    status = db.Column(db.String(255))
    due_date = db.Column(db.Date)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Payment(id={self.id}, " \
               f"company='{self.company}', " \
               f"amount={self.amount}, " \
               f"payment_date='{self.payment_date}', " \
               f"status='{self.status}', " \
               f"due_date='{self.due_date}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'amount': self.amount,
            'payment_date': self.payment_date.isoformat() if self.payment_date else None,
            'status': self.status,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
