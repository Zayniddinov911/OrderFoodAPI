from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


# User Model
class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    username = Column(String(24), unique=True)
    email = Column(Text, unique=True)
    password = Column(Text, nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='user')


    def __repr__(self):
        return f'<User {self.username}>'
    
class Order(Base):

    ORDER_STATUSES = (
        ('PENDING', 'pending'),
        ('ON-THE-WAY', 'on the way'),
        ('DELIVERED', 'delivered')

    )

    PIZZA_SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),

    )


    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default='PENDING')
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default='SMALL')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f'<Order {self.id}>'