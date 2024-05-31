from fastapi import APIRouter, Response
from app.models.request_models import GetCurrentWeatherRequest
from app.services.weather_service import get_weather_by_city

router = APIRouter()


@router.post("/getCurrentWeather")
async def get_current_weather(data: GetCurrentWeatherRequest):
    weather_data = get_weather_by_city(data.city)

    if weather_data is None:
        return {"message": "Failed to fetch weather data."}

    if data.output_format == 'json':
        result = {
            "Weather": f"{weather_data.current.temp_c} C",
            "Latitude": str(weather_data.location.lat),
            "Longitude": str(weather_data.location.lon),
            "City": f"{weather_data.location.name} {weather_data.location.country}"
        }
        return result
    elif data.output_format == 'xml':
        xml_data = f"""<?xml version="1.0" encoding="UTF-8" ?>
        <root>
            <Temperature>{weather_data.current.temp_c}</Temperature>
            <City>{weather_data.location.name}</City>
            <Latitude>{weather_data.location.lat}</Latitude>
            <Longitude>{weather_data.location.lon}</Longitude>
        </root>
        """
        return Response(content=xml_data, media_type="application/xml")
    else:
        return {"message": "Invalid output format. Supported formats: json, xml"}
