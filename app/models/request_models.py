from __future__ import annotations

from pydantic import BaseModel


class GetCurrentWeatherRequest(BaseModel):
    city: str
    output_format: str
