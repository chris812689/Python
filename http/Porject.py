import requests
from random import choice
url = "https://icanhazdadjoke.com/search"
term = input("What would you like to search for?")

res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params= {"term": term}
    
    ).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes >= 1:
    print(f"We found {num_jokes} with {term}. Here is one")
    print(choice(results)["joke"])
else:
    print(f"Sorrym there are no jokes for {term}")