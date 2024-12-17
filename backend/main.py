from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
import os

app = FastAPI()

# Use the absolute path to the frontend folder
frontend_path = os.path.abspath("C:\Users\aaa\Documents\Projects\ChatBot\frontend")

# Mount the static files
app.mount("/static", StaticFiles(directory=frontend_path, html=True), name="static")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the chatbot app!"}
