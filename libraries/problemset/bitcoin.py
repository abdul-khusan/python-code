import requests
import sys 
import json


try:
      response = requests.get("https://api.frankfurter.dev/v2/rate/krw/usd" )
      data = response.json()
      rate = data['rate']

      user_krw = float(sys.argv[1])
      converted_usd = user_krw * rate

      print(f"${converted_usd}")

except (ValueError, IndexError, requests.RequestException):
      print('Invalid')