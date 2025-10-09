from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

SERVICES = {
    "add": "http://add-service:8001/add",
    "subtract": "http://subtract-service:8002/subtract",
    "multiply": "http://multiply-service:8003/multiply",
    "divide": "http://divide-service:8004/divide"
}

@app.get("/calc")
def calculate(op: str, a: float, b: float):
    if op not in SERVICES:
        raise HTTPException(status_code=400, detail="Unknown operation")
    url = SERVICES[op]
    resp = requests.get(url, params={"a": a, "b": b})
    return resp.json()
