"""
get stock data
"""
import requests
from main import dot


def get_stock_data(symbol):

    params = {
      'access_key': dot.get("ACCESS_KEY")
    }

    api_result = requests.get(f'https://api.marketstack.com/v1/tickers/{symbol}', params)

    api_response = api_result.json()
    print(api_response)
    return api_response['data']

