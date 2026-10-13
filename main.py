#  main gate for the project 

from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    return  {
            "message":"Hello World! - testing reload"
        }
