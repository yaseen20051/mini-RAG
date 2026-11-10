from fastapi import FastAPI, APIRouter 
import os

base_router = APIRouter(
    prefix="/api/revision",  ## عشان لو اطلب تحط بريفيكس معين,
    tags=["revision"]
)


@base_router.get("/") ### this is called routes  specific feature or page 
def welcome():
    
    return {
        "message" : "Hello All !!"
    }

@base_router.get("/app_details")
def app_details():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    return {
        "app name " : app_name ,
        "app_version " : app_version
    }