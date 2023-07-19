from pydantic import BaseModel
from typing import Optional, ClassVar
from uuid import UUID, uuid4
from sqlalchemy.orm import mapped_column, Mapped
from typing_extensions import Annotated

intpk = Annotated[int, mapped_column(primary_key=True)]

class SignUpModel(BaseModel):

    __abstract__ = True
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    is_staff: Optional[bool]
    is_active: Optional[bool] 
    orders: Optional[bool] 

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': 'johndoe',
                'email': 'johndoe@gmail.com',
                'password': 'password',
                'is_staff': False,
                'is_active': True
            }
        }

    


        