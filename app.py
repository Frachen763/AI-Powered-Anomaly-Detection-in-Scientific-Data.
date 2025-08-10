from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI()

class SensorReading(BaseModel):
    timestamp: float
    temperature: float
    pressure: float
    current: float

@app.post("/api/data")
async def ingest(reading: SensorReading):
    # TODO: Add DB insert and anomaly detection
    return {"status": "ok", "received": reading.dict()}
