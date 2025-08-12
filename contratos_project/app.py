import os

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from .routes import router

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, 'templates'))
app.include_router(router)
