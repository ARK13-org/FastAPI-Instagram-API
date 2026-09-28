from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db.database import engine
from db.models import base
from routers import user , post , comment
from auth import authentication

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

app.mount("/files", StaticFiles(directory="uploaded_file"), name="files")

base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return 'first page'