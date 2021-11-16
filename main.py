from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import Todo

# app object
app = FastAPI()

from database import (
     fetch_one_todo,
     fetch_all_todos,
     create_todo,
     update_todo,
     remove_todo,
 )

origins = ['http://localhost:5055']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials = True,
    allow_methods=["*"], 
    allow_headers=["*"],
)




# get

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

# get by id

@app.get("/api/todo/{order_email}",response_model=Todo)
async def get_todo_by_id(order_email):
    response = await fetch_one_todo(order_email)
    if response: 
        return response
    raise HTTPException(404, f"there is no TODO item with this title{order_email}")

# post

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "something went wrong / Bad request")

# update

@app.put("/api/todo/{order_email}",response_model=Todo)
async def put_todo(order_email:str, status:str):
    response = await update_todo(order_email, status)
    if response: 
        return response
    raise HTTPException(404, f"there is no TODO item with this title {order_email}")

# delete

@app.delete("/api/todo{order_email}")
async def delete_todo(order_email):
    response = await remove_todo(order_email)
    if response:
        return "Succesfully deleted todo item !"
    raise HTTPException(404, f"there is no TODO item with this title {order_email}")
