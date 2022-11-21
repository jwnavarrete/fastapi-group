from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import  user, auth, Category, Privacy, Group

from . import models
from .database import engine
from .config import settings
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(Category.router)
app.include_router(Privacy.router)
app.include_router(Group.router)


#app.include_router(post.router)
#app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}