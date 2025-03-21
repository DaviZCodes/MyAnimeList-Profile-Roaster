import os
from openai import OpenAI
from dotenv import load_dotenv 

load_dotenv() 

# getting the GITHUB_TOKEN from the env 
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)

def generateRoast(): 
    file = open("user_output.txt", "r")

    file_content = file.read()

    prompt = "Can you roast this user's MAL profile? Make sure to laugh at the user and be funny and sarcastic. You don't have to mention every piece of information I included, but just roast some useful and relevant things. Make sure the roast is not that long. Make fun of the user for their taste, call the user arrogant for giving low scores, and tell the user to go touch grass if they watch too much anime. Do not include anything offensive like slurs though." + file_content

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o",
        temperature=1,
        max_tokens=4096,
        top_p=1
    )

    return response.choices[0].message.content