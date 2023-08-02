import requests


request = requests.post(
    url="http://127.0.0.1:5000/json",
    # json=scrape()
)

print(request.text)
