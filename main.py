from fastapi import FastAPI,HTTPException
from models import Product 

app = FastAPI()

@app.get('/')
def gethome():
    return 'welcome to the crud api server  home page '


products_list = [
    Product(id=1, name='ball', description ='to play game', price=250.00),
    Product(id=2, name='bat', description ='to hit ball in game', price=450.00)
    ]


@app.get('/products')
def get_all_products():
    return products_list

@app.get('/product/{id}')
def get_product(id: int):
    for product in products_list:
        if product.id == id :
            return product
    raise HTTPException(status_code=404, detail="No product found")

@app.post('/product')
def add_product(product : Product):
    products_list.append(product)
    return products_list

@app.delete('/product/{id}')
def delete_product(id : int):
     product_tobe_deleted = get_product(id)
     products_list.remove(product_tobe_deleted)
     return products_list

@app.put("/product/{id}")
def update_product(id: int, product : Product):
   product_tobe_updated = get_product(id)
   index = products_list.index(product_tobe_updated)
   products_list.remove(product_tobe_updated)
   products_list.insert(index,product)
   return products_list

    