from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add_number")
async def too_many_letters(x,y):
    return int(x)+int(y)