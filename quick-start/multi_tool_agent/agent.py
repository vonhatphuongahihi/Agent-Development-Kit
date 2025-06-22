import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def get_weather(city: str) -> dict:
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": "Thời tiết ở New York là nắng, 25°C (77°F)."
        }
    else:
        return {
            "status": "error",
            "message": f"Không có thông tin thời tiết cho {city}"
        }

def get_current_time(timezone: str) -> dict:
    if timezone.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": f"Xin lỗi, không có thông tin múi giờ cho {city}."
        }
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"Giờ hiện tại ở {city} là {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}

root_agent = Agent(
    name = "weather_time_agent",
    model = "gemini-2.0-flash",
    description = "Trợ lý trả lời câu hỏi về thời tiết và thời gian.",
    instruction = "Bạn là một trợ lý hữu ích có thể trả lời câu hỏi về thời tiết và thời gian.",
    tools = [get_weather, get_current_time]
    )
