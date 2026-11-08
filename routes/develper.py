from fastapi import FastAPI,APIRouter
import os 
developer_router = APIRouter(
    prefix= "/developer",
    tags=["Develper page"]
)

developer_name = os.getenv('DEVELOPER_NAME')
developer_age = os.getenv('DEVELOPER_AGE')

@developer_router.get("/")
async def developer_welcome():
    return {"Welcome page" : "welcome to the develpe page"}

@developer_router.get("/age") 
async def get_developer_age():
    return {"developer age" : developer_age}

@developer_router.get("/name") 
async def get_developer_name():
    return {"developer name" : developer_name}
 

    