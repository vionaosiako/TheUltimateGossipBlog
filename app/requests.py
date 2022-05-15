
import urllib.request,json

import requests
from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    Function that consumes http request and returns random quotes
    """
    response = requests.get(url).json()
    random_quote = Quote(response.get("author"), response.get("quote"))
    
    return random_quote


    
    
