import os
import openai

def init_api():
# reading variables from .env file, namely API_KEY and ORG_ID.
    with open(".env") as env:
        for line in env:
            key, value = line.strip().split("=")
            os.environ[key] = value
# Initializing the API key and organization id
    openai.api_key = os.environ.get("API_KEY")
    openai.organization = os.environ.get("ORG_ID")

init_api()

next = openai.Completion.create(
    model="text-davinci-002",
    prompt="Write a JSON containing primary number between 0 to 9 \n\n{\n\t\"prim\
es\": [",
    suffix="]\n}"
)

print(next)