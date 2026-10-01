from pydantic import BaseModel

class Product(BaseModel) :
    id : int
    name : str
    description: str
    price : float
# constructer for the model class to bind the passed values 
    # def __init__(self, id, name, description, price ):
    #     self.id = id
    #     self.name = name 
    #     self.description = description
    #     self.price = price

#  with pydantic base model we dont need the constructer 