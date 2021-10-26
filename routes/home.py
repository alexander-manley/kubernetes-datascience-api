# Router template
from fastapi import APIRouter
app_home = APIRouter()


@app_home.get('/', tags=["Intro"])
async def home():
    return {"message": "/"}


@app_home.get('/route1', tags=["Intro"])
async def ml1():
    return {"message": "/ml1"}
