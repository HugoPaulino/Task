import json
from fastapi import FastAPI
from ..app import app

from fastapi.testclient import TestClient

#app = FastAPI()

client = TestClient(app)



def test_classify_article():
    data = {"article":"EMTEC TAKE IT EASY 8 GB 100X, BIS 15 MB/S"}
    response = client.post("/predict_productgroup",json="EMTEC TAKE IT EASY 8 GB 100X, BIS 15 MB/S")
    
    assert response.status_code == 200 
    assert response.json()["text_message"] == "EMTEC TAKE IT EASY 8 GB 100X, BIS 15 MB/S"
    assert response.json()["product_group"] == "USB MEMORY"
    assert response.json()["confidence_score"] == "0.9752715"