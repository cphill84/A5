
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .dependencies.database import engine, get_db
from . import models, schemas
from .controllers import orders, resources, order_details, recipes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Orders Endpoints
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create_order(db=db, order=order)

@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.get_all_orders(db)

@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.get_order(db=db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return orders.update_order(db=db, order_id=order_id, order=order)

@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return orders.delete_order(db=db, order_id=order_id)

# Resources Endpoints
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create_resource(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.get_all_resources(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.get_resource(db=db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update_resource(db=db, resource_id=resource_id, resource=resource)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.delete_resource(db=db, resource_id=resource_id)

# Order Details Endpoints
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["Order Details"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create_order_detail(db=db, order_detail=order_detail)

@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["Order Details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.get_all_order_details(db)

@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def read_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.get_order_detail(db=db, order_detail_id=order_detail_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return order_detail

@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
def update_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details.update_order_detail(db=db, order_detail_id=order_detail_id, order_detail=order_detail)

@app.delete("/order_details/{order_detail_id}", tags=["Order Details"])
def delete_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    return order_details.delete_order_detail(db=db, order_detail_id=order_detail_id)

# Recipes Endpoints
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create_recipe(db=db, recipe=recipe)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_recipes(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.get_recipe(db=db, recipe_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    return recipes.update_recipe(db=db, recipe_id=recipe_id, recipe=recipe)

@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes.delete_recipe(db=db, recipe_id=recipe_id)

