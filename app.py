from fastapi import FastAPI, Request #importo la classe da una libreria 
from routes import router
import time

app = FastAPI() #costruttore di default della classe FastAPI 
app.include_router(router)

@app.middleware("http")
async def measure_latency(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    elapsed_ms = (time.time() - start) * 1000
    print(f"Latency: {elapsed_ms:.2f} ms")
    return response

@app.get("/")
def read_root():
    return{"bella"}

@app.get("/health")
def health():
    return {"status": "ok"}