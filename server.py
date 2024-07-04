import requests as requests

data = {
    "engine_temperature": 0.3,
}

response = requests.post("http://127.0.0.1:8000/record", json=data)
print(response.content)