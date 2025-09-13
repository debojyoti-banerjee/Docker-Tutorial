from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from app.predictor import predictor

app=FastAPI()
prediction=predictor()

class features(BaseModel):
    features:list[float]
    
@app.post("/predict")
def predict(data:features):
    try:
        result=prediction.predict(data.features)
        return {"prediction":int(result)}
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    