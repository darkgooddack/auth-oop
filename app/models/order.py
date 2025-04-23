from sqlalchemy import Column, Integer, ForeignKey, Enum, Numeric, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.db.init_db import Base

class OrderStatus(enum.Enum):
    none = "none"
    created = "created"
    paid = "paid"
    ready = "ready"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    random_number = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.none)
    total_price = Column(Numeric(10, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime, nullable=True)

    items = relationship("OrderItem", back_populates="order")