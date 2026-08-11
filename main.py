import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

# Create GRoq Client

client = Groq(
    api_key = GROQ_API_KEY
)



def agent(query):
    response = client.chat.completions.create(
        model = GROQ_MODEL,
        messages=[
            {
                "role":"user",
                "content": query
            }
        ]
        
    )

    return response.choices[0].message.content

query = input("You: ")

answer = agent(query)
print("Agent:", answer)