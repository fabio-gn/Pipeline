from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def read_root():
    return{"bella"}
@app.get("/health")
def health():
    return {"status": "ok"}