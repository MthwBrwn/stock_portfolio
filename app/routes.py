from . import app
import requests as req

def get_stock_info(code):
    return req.get(f"{os.getenv('API_URL')}{code}&APPID={os.getenv('API_KEY')}")
