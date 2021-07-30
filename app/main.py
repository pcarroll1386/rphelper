from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the RP helper! get excited! ... or don't it is your life."}