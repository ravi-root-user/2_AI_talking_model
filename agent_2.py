import os
import openai as ai

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

apikey = "your open AI key"
ai.api_key = apikey
model_engin = 'text-davinci-003'
with open('myfile.txt', 'r') as file:
    content = file.read()
    prompt = ["Act as Morty from 'Rick & Morty' show. try to be funny and talk to your grandfather rick"
              "story that is not in any episode ",content]

completion = ai.Completion.create(
    engine=model_engin,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
response = completion.choices[0].text

with open('myfile.txt', 'w') as file:
    file.write(response)
print(G + response)

os.system("python3 agent_1.py")

