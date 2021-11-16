from pydantic import BaseModel 

class Todo(BaseModel):
    order_date: str
    order_number: str
    order_email: str
    order_mobile: str 
    brand: str 
    model: str 
    colors: str 
    capacity: str 
    payment: str
    status: str
