from app.tools.calculator import calculate
from app.tools.weather import get_weather
from app.tools.websearch import search_web

TOOL_REGISTRY = {
    "get_weather" : get_weather,
    "calculate" : calculate,
    "search_web" : search_web,
}

