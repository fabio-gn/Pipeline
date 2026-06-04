from fastapi import FastAPI #importo la classe da una libreria 
from routes import router

app = FastAPI() #costruttore di default della classe FastAPI 
app.include_router(router)

@app.get("/")
def read_root():
    return{"bella"}

@app.get("/health")
def health():
    return {"status": "ok"}