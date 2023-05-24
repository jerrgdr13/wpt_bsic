#!/usr/bin/env python3
import requests
import config

url = "https://jguerra-origin.akamaidemos.com/"  # The URL you want to run a test on
endpoint = f'https://www.webpagetest.org/runtest.php?url={url}&f=json'
response = requests.get(endpoint)
print(response.json())

'''@app.get("/")
def index():
    return {"name": "First Data"}


@app.post("/create-wpt/{url}")
def create_wpt(url: str, testdt : Testdt):
    
    test_url = url

    test_options = {
        "label" : 'Jguerra test',
        "k": config.wpt_api_key,
        "f": "json",
        "runs": 1,
        "location": "ec2-eu-central-1.4G",
        "desktop": 1,
    }

endpoint = f'https://www.webpagetest.org/runtest.php?url={test_url}'
response = requests.get(endpoint, params=test_options)

# Do something with the response
print(response.json())
