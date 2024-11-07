from fastapi import FastAPI
from fastapi.responses import JSONResponse
# from contextlib import asynccontextmanager
from scrape import run
import json
# import os

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await run()
#     yield

# app = FastAPI(lifespan=lifespan)
app = FastAPI()

# app.router.lifespan_context = lifespan

def load_repositories_data():
    with open("repositories.json", "r") as f:
        return json.load(f)

# with open("repositories.json", "r") as f:
#     repositories_data = json.load(f)

def load_developers_data():
    with open("developers.json", "r") as f:
        return json.load(f)

# with open("developers.json", "r") as f:
#     developers_data = json.load(f)

@app.get("/trending-repositories")
def get_trending_repositories():
    repositories_data = load_repositories_data()
    return JSONResponse(content=repositories_data, status_code=200)

@app.get("/trending-developers")
def get_trending_developers():
    developers_data = load_developers_data()
    return JSONResponse(content=developers_data, status_code=200)