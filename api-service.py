from fastapi import FastAPI
from joblib import load
from routes.v1.app1 import app_predict_v1
from routes.home import app_home
import models.ml.classifier as clf

app = FastAPI(title="ML API", description="ML model API", version="1.0")


@app.on_event('startup')
async def load_model():
    clf.model = load('models/ml/data_dt_v1.joblib')


app.include_router(app_home)
app.include_router(app_data_predict_v1, prefix='/v1')
