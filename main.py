import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


#####################################

#  TOOLS 

##########################################

def get_weather(city:str):
    return f"The Weather in {city} is 30 degree and sunny."

def calculator(expression:str):
    return str(eval(expression))

def search_web(query:str):
    return f"Search Results for: {query}"

