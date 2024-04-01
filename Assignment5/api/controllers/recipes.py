from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .dependencies.database import engine, get_db
from . import models, schemas
from .controllers import orders, resources, order_recipes, order_details, recipes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create_recipe(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.get_all_recipes(db=db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
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
