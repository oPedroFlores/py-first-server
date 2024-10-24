from fastapi import FastAPI
from Routes import user  

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API ON!"}

app.include_router(user.router)
