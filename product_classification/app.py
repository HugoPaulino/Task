# Load the libraries
from fastapi import FastAPI, HTTPException
from joblib import load
import numpy as np
# Load the model
product_group_clf = load(open('./models/product_classification_model_v0.1.pkl','rb'))

# Initialize an instance of FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Product Group Classification API"}

# Define the route to the sentiment predictor
@app.post("/predict_productgroup")
def predict_productgroup(article: str):

    if(not(article)):
        raise HTTPException(status_code=400, 
                            detail = "Please Provide a valid text message")

    prediction = product_group_clf.predict([article])
    confidence_score = product_group_clf.predict_proba([article])

    confidence = str(confidence_score[0][np.argmax(confidence_score)])
    
    return {
            "text_message": article, 
            "product_group": prediction[0],
            "confidence_score": confidence
           }
