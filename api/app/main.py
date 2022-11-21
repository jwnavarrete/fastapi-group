from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import  formula, post, parametro, parametroDetalle, grupo, subGrupo, user, auth, vote, perfil, logs, tipo, rubro, formulaDetalle, menu, menuPerfil

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

app.include_router(perfil.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(tipo.router)
app.include_router(formula.router)
app.include_router(rubro.router)
app.include_router(menu.router)
app.include_router(logs.router)
app.include_router(formulaDetalle.router)
app.include_router(menuPerfil.router)
app.include_router(parametro.router)
app.include_router(parametroDetalle.router)
app.include_router(grupo.router)
app.include_router(subGrupo.router)



#app.include_router(post.router)
#app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}