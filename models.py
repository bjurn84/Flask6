from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: str
    order_status: str

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float