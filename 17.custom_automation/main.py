import requests
import random
from dotenv.main import DotEnv
from twilio.rest import Client

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

account_sid = dot.get("TWILIO_ACCOUNT_SID")
auth_token = dot.get("TWILIO_AUTH_TOKEN")
my_twilio_phone = dot.get("MY_TWILIO_NUMBER")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                body=f"Joke: {joke_data['joke']}\n\nQuote: {quote_data['text']} -by {quote_data['author']}",
                from_=my_twilio_phone,
                to="+91 73833 67995",
            )

print(message.sid)
