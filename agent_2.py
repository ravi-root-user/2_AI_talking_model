import os
import openai as ai

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

apikey = "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"
ai.api_key = apikey
model_engin = 'text-davinci-003'
with open('myfile.txt', 'r') as file:
    content = file.read()
    prompt = ["Act as Morty from 'Rick & Morty' show. Keep the line as short conversation wait before answering back "
              "in the convo",content]
max_tokens_per_line = 10
completion = ai.Completion.create(
    engine=model_engin,
    prompt=prompt,
    max_tokens=max_tokens_per_line,
    n=1,
    stop=None,
    temperature=0.5,
)
response = completion.choices[0].text
print(response)
with open('myfile.txt', 'w') as file:
    file.write(response)
print(R + response)
print("hello from agent 2")
# os.system("python3 agent_1.py")
print("bye from agent 2")
