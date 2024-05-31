from fastapi import FastAPI
import uvicorn
from app.api.weather import router as weather_router

app = FastAPI(
    title="Weather API",
    version="0.1",
    description="An API to get current weather data, assignment for Verloop.io",
)
app.include_router(weather_router)

if __name__ == "__main__":
    uvicorn.run(app)
