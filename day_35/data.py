import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean", params=parameters) #Generate your API here https://opentdb.com/api_config.php with True/False answers
response.raise_for_status()
data = response.json()
question_data = data["results"]
