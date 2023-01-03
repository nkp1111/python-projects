import requests
import random
from dotenv.main import DotEnv

dot = DotEnv(".env")

url_for_joke = "https://api.humorapi.com/jokes/random"
param = {
    "api-key": dot.get("API_KEY")
}
response = requests.get(url_for_joke, params=param)
joke_data = response.json()

url_for_quote = "https://type.fit/api/quotes"
response = requests.get(url_for_quote)
quotes = response.json()
quote_data = random.choice(quotes)

print(joke_data, quote_data)





