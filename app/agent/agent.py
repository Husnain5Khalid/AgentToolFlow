from groq import Groq

from app.config.settings import GROQ_API_KEY,GROQ_MODEL

from app.executor.executor import ToolExecutor


class Agent:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        self.tool_executor = ToolExecutor()

    def get_tools(self):
        return [
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a city.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": "The name of the city."
                            }
                        },
                        "required": ["city"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "calculate",
                    "description": "Calculate a mathematical expression.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "expression": {
                                "type": "string",
                                "description": "The mathematical expression."
                            }
                        },
                        "required": ["expression"]
                    }
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "search_web",
                    "description": "Search the web for information.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query."
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        ]

    def run(self, query:str):
        messages = [
        {
            "role":"user",
            "content": query,
        }
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.get_tools(),
            tool_choice="auto",

        )
        assistant_message = response.choices[0].message

        if not assistant_message.tool_calls:
            return assistant_message.content

        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name
            arguments = tool_call.function.arguments

            result = self.tool_executor.execute(
                tool_name,
                arguments,
            )

            print(f"Tool called: {tool_name}")
            print(f"Tool result: {result}")
    

    