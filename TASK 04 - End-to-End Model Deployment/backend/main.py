# # backend/main.py

# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
# import numpy as np
# import uvicorn

# # Load model and scaler
# model = joblib.load("C:\Users\kaveethaj\Downloads\BlueChip Documents\TASK 04 - End-to-End Model Deployment\backend\model\personality_model.pkl")
# scaler = joblib.load("C:\Users\kaveethaj\Downloads\BlueChip Documents\TASK 04 - End-to-End Model Deployment\backend\model\scaler.pkl")

# app = FastAPI()

# class InputData(BaseModel):
#     Time_spent_Alone: float
#     Stage_fear: str
#     Social_event_attendance: float
#     Going_outside: float
#     Drained_after_socializing: str
#     Friends_circle_size: float
#     Post_frequency: float

# @app.post("/predict")
# def predict(data: InputData):
#     features = np.array([[data.Time_spent_Alone, data.Stage_fear, data.Social_event_attendance,
#                           data.Going_outside, data.Drained_after_socializing,
#                           data.Friends_circle_size, data.Post_frequency]])
    
#     features_scaled = scaler.transform(features)
#     prediction = model.predict(features_scaled)[0]
    
#     personality = "Extrovert ✨" if 1 == 1 else "Introvert 🌙"
#     return {"personality_type": personality}

# # Uncomment below to run with `python main.py`
# # if __name__ == "__main__":
# #     uvicorn.run(app, host="127.0.0.1", port=8000)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn
from pathlib import Path

# Get the directory of the current script
BASE_DIR = Path(__file__).resolve().parent

# Define relative paths
MODEL_PATH = BASE_DIR / "model" / "personality_model.pkl"
SCALER_PATH = BASE_DIR / "model" / "scaler.pkl"

# Load model and scaler with error handling
try:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    if not SCALER_PATH.exists():
        raise FileNotFoundError(f"Scaler file not found at {SCALER_PATH}")
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    raise Exception(f"Failed to load model or scaler: {str(e)}")

app = FastAPI()

class InputData(BaseModel):
    Time_spent_Alone: float
    Stage_fear: int
    Social_event_attendance: float
    Going_outside: float
    Drained_after_socializing: int
    Friends_circle_size: float
    Post_frequency: float

@app.post("/predict")
async def predict(data: InputData):
    try:
        # Convert input data to numpy array
        features = np.array([[
            data.Time_spent_Alone,
            data.Stage_fear,
            data.Social_event_attendance,
            data.Going_outside,
            data.Drained_after_socializing,
            data.Friends_circle_size,
            data.Post_frequency
        ]])
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        
        # Map prediction to personality type
        personality = "Extrovert ✨" if prediction == 1 else "Introvert 🌙"
        
        return {"personality_type": personality}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")

# Uncomment below to run with `python main.py`
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)