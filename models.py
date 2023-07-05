from pydantic import BaseModel
from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

class Food(str, Enum):
    Pizza = "Pizza"
    Burger = "Burger"
    Sandwiches = "Sandwiches"
    Plov = "Plov"


class User(str, BaseModel):
    id: Optional[UUID] = uuid4
    name: str
    address: str


class Order(int, str, BaseModel):
    id: Optional[UUID] = uuid4
    food: Optional[Food]
    user: List[User]






