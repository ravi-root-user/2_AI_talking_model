import openai as ai
import os

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow

apikey = "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"
ai.api_key = apikey
model_engin = 'text-davinci-003'
prompt = [
    "Talk & Keep the sentence short wait before answering back in the conversation"]
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
print("hello from agent 1")
print(G + response)
print("Writing into file")
with open('myfile.txt', 'w') as file:
    file.write(response)
print("Writing done\nCalling 2nd program")
os.system("python3 agent_2.py")
print("bye from agent 1")

