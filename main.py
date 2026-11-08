from fastapi import FastAPI 

from dotenv import load_dotenv ## in the main so all routes see it 
load_dotenv(".env")  ## store all values in the system 

from routes import base


app = FastAPI()

app.include_router(base.base_router)



### main.py el saf7a el ra2esya must not have so much details 
## so we make routes
