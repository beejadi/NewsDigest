import requests
import os
api_key=os.environ.get('API_KEY')

if api_key is None:
    raise ValueError("Key Not found")
url="https://newsapi.org/v2/everything?q=tesla&from=2023-11-14&sortBy=publishedAt&apiKey="+api_key

response=requests.get(url)
content=response.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"],"\n")

