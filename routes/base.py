## this is for default routes such as the / and /welcome 
from fastapi import FastAPI , APIRouter 
import os

base_router = APIRouter(
        prefix="/api/v1" ,## all routes must get called by this ,
        tags= ["api_v1_ML"]


)  ## SAME AS FastAPI() But APIRouter for routes



@base_router.get("/")

def main_page():
    app_name = os.getenv('APP_NAME')  
    app_version = os.getenv('APP_VERSION')
    ## SAME NAME IN THE .ENV but how did he get it ??
         #  its from the load_dotenv in the main  
    return { 
        "app_name " : app_name,
        "app_version": app_version
        }