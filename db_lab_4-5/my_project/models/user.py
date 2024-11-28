# models/user_dao.py
from sqlalchemy import Column, Integer, String, Date, Enum, DECIMAL
from my_project import db

class User(db.Model):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    user_type = Column(Enum('renter', 'owner'), nullable=False)
    account_balance = Column(DECIMAL(10, 2), default=0.00)
    registration_date = Column(Date, nullable=False)
