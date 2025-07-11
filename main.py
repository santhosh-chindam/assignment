from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "ee33858a8b121416d9d5918d96267b98" 
CURRENCY_API = "https://api.exchangerate.host/convert"

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    currencies = ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "CHF"]
    return templates.TemplateResponse("index.html", {"request": request, "currencies": currencies})

@app.get("/convert")
async def convert(
    from_currency: str = Query(...),
    to_currency: str = Query(...),
    amount: float = Query(...)
):
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "access_key": API_KEY
    }
    try:
        response = requests.get(CURRENCY_API, params=params)
        print("Request URL:", response.url)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        data = response.json()

        if response.status_code == 200 and data.get("success", False):
            return {"converted_amount": data["result"]}
        else:
            return {
                "error": "Conversion failed or invalid input",
                "api_response": data
            }

    except Exception as e:
        return {"error": f"An exception occurred: {str(e)}"}
