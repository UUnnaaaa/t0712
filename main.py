from fastapi import FastAPI
from fastapi.testclient import TestClient
import shopping

app = FastAPI()


@app.get("/")
def read_main():
    return {"msg": "Hello World"}

def get_pricing(obj):
    return obj["pricing"]
    
@app.get("/pricing")
def pricing(keyword: str, sort_by: str = None):
    eslite_data = shopping.query_eslite(keyword)
    pchome_data = shopping.query_pchome(keyword)
    data = pchome_data + eslite_data
    if sort_by == "-pricing":
        data.sort(key=get_pricing)
        # data = sorted(data, key=get_pricing)
    return data
