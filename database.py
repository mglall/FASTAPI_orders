from model import Todo

# mongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://mglall:Mm0509329943@mg.m8axd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

database = client.TodoList
collection = database.todo

async def fetch_one_todo(order_email):
    document = await collection.find_one({"order_email":order_email})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos 

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(order_email,status):
    await collection.update_one({"order_email":order_email},{"$set":{
        "status":status}})
    document = await collection.find_one({"order_email":order_email})
    return document

async def remove_todo(order_email):
    await collection.delete_one({"order_email":order_email})
    return True