# models.py
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Expense(db.Model):
    __tablename__ = "expenses"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(64), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.date.today)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Expense id={self.id} category={self.category} amount={self.amount}>"
