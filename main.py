import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth import authentication
from db.database import engine, run_light_migrations
from db.models import base
from routers import comment, post, user

os.makedirs("uploaded_file", exist_ok=True)

app = FastAPI(title="Instagram API")
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

app.mount("/files", StaticFiles(directory="uploaded_file"), name="files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base.metadata.create_all(bind=engine)
run_light_migrations()
