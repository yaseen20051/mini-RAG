from fastapi import FastAPI
app = FastAPI()


@app.get("/")   ## decorater 
def welcome():
    return {
        "message": "Hello World !!!!"
    }
@app.get("/main_page")
def main_page():
    return {
        "message": "you are in the main page"
    }