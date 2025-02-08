from fastapi import FastAPI

app = FastAPI(host="0.0.0.0")

@app.get("/")
def read_root():
    return {"Please": "reload page ..."}
