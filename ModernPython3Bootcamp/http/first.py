import requests
url = "https://icanhazdadjoke.com"

response = requests.get(url, headers={"Accept": "application/json"})

print(f"Your request to icanhazdadjoke came back w/ status code {response.status_code}")

data = response.json()

print(type(data))
print(data["joke"])
