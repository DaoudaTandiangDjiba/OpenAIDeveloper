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

# Calling the API and listing models
next = openai.Completion.create(
    model ="text-davinci-001",
    prompt="once upon a time",
    max_tokens=5,
    #n=1,
    #best_of=2,
    stop=["\n","Story", "End", "Once upon a time"],
)
print(next)