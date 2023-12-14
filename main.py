import requests
url="https://newsapi.org/v2/everything?q=tesla&from=2023-11-14&sortBy=publishedAt&apiKey=fac220e0d4fb47788c229b4993db0bfd"
response=requests.get(url)
content=response.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])

