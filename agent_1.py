import openai as ai
import os
import time

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white
Y = '\033[33m'  # yellow


def api_call(prompt):
    apikey = "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"
    ai.api_key = apikey
    model_engin = 'text-davinci-003'

    completion = ai.Completion.create(
        engine=model_engin,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text

    print(R + response)

    with open('myfile.txt', 'w') as file:
        file.write(response)
    time.sleep(62)
    os.system("python3 agent_2.py")


has_executed = False
if not has_executed:
    # Execute the code or action you want to run once
    with open('myfile.txt', 'r') as file:
        content = file.read()
        line1 = "Act as rick from 'Rick & Morty' show. try to be funny and talk to your grandson morty"
        prompt = [line1, content]
        api_call(prompt)

    # Set the flag to True to indicate that it has executed
    has_executed = True
else:
    with open('myfile.txt', 'r') as file:
        content = file.read()
        prompt = [content]
        api_call(prompt)
