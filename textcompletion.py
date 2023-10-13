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
    max_tokens=100,
    #top_p=.9,
    #temperature=2,
    #logprobs=2,
    #stream=True,
    frequency_penalty=2.0,
    presence_penalty=2.0,
)
print("=== Frequency and presence penalty 2.0 ===")
print(next["choices"][0]["text"])

next = openai.Completion.create(
    model ="text-davinci-001",
    prompt="once upon a time",
    max_tokens=100,
    frequency_penalty=-2.0,
    presence_penalty=-2.0,
)
print("=== Frequency and presence penalty -2.0 ===")
print(next["choices"][0]["text"])
#print(type(next))
#print(models)
#print(*next, sep='\n')
#for i in next:
    #print(i['choices'][0]['text'])