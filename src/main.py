from fastapi import FastAPI, APIRouter


app = FastAPI()
router = APIRouter()

#Forma tradicional de criar uma api
#@app.router.get('/')

#Usando o router
@router.get('/')
def first():
    return 'Hello World'

#Usando router para incluir um prefixo (fica mais organizado)
app.include_router(prefix='/first', router=router)
