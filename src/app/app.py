from fastapi import FastAPI, HTTPException
from src.pred.image_classifier import tf_run_classifier
from pydantic import BaseModel

app = FastAPI(title="Traffic Sign Recognition API")

class Img(BaseModel):
    img_url: str

@app.post("/predict/tf/", status_code=200)
async def predict_tf(request: Img):
    prediction = tf_run_classifier(request.img_url)
    if not prediction:
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"
        )
    return prediction