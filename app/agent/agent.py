from groq import Groq

from app.config.settings import GROQ_API_KEY,GROQ_MODEL

class Agent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL

        