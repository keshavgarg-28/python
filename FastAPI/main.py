from fastapi import FastAPI, Path, HTTPException
from mockdata import products
from pydantic import BaseModel
from dtos import ProductDto
import json

app=FastAPI()

def load_data():
    with open("data.json","r") as f:
        data=json.load(f)
    return data

@app.get("/")
def Hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def About():
    return {"message":"A Fully Functional App to maintain patients record."}

## Get method to retrieve all records of patient
@app.get("/view")
def View():
    data=load_data()
    return data


## Path Parameter to get record of particular patient
@app.get("/patient/{patient_id}")
def Patient(patient_id:str = Path(..., description="Id of patient in db", example="P001")):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    ##return {"error":"Patient not found."}
    raise HTTPException(status_code=404, detail="Patient not found.")

## Query Parameter
@app.get("/sort")
def sort(sort_by:str, order:str):
    valid_fields=["Height","Weight"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Enter valid fields")
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400, detail="Enter valid fields")
    data=load_data()
    sort_order= True if order=="desc" else False
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data

@app.post("/create")
def create_product(product_Data: ProductDto):
    product_Data=product_Data.model_dump()
    products.append(product_Data)
    return{"status":"Product Created Successfully","data":products}

@app.get("/see")
def viewprod():
    return products

@app.put("/update/{product_id}")
def update_prod(product_data:ProductDto, product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id")==product_id:
            products[index] = product_data

    return{"status":"Product Updated Successfully"}

@app.delete("/delete/{product_id}")
def delete_prod(product_id: int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id")==product_id:
            delete_prod=products.pop(index)
            return{"status":"Deleted"}