from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.database import engine
from db.models import base
from routers import user , post , comment
from auth import authentication
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
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