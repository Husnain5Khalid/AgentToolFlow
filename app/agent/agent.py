from groq import Groq

from app.config.settings import GROQ_API_KEY, GROQ_MODEL
from app.executor.executor import ToolExecutor


class Agent:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL
        self.tool_executor = ToolExecutor()

    def get_tools(self):
        """
        Return the tool schemas that are exposed to the LLM.
        """

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
                                "description": "The name of the city.",
                            }
                        },
                        "required": ["city"],
                    },
                },
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
                                "description": "The mathematical expression to calculate.",
                            }
                        },
                        "required": ["expression"],
                    },
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
                                "description": "The search query.",
                            }
                        },
                        "required": ["query"],
                    },
                },
            },
        ]

    def run(self, query: str) -> str:
        """
        Run the agent for a user query.

        The agent repeatedly:
        1. Sends the conversation to the LLM.
        2. Checks whether the LLM wants to call a tool.
        3. Executes requested tools.
        4. Sends tool results back to the LLM.
        5. Stops when the LLM produces a final answer.
        """

        messages = [
            {
                "role": "user",
                "content": query,
            }
        ]

        while True:

            # ---------------------------------
            # Ask the LLM what to do
            # ---------------------------------

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.get_tools(),
                tool_choice="auto",
            )

            assistant_message = response.choices[0].message

            # ---------------------------------
            # Store the assistant's decision
            # ---------------------------------

            messages.append(assistant_message)

            # ---------------------------------
            # No tool required
            # Agent has the final answer
            # ---------------------------------

            if not assistant_message.tool_calls:
                return assistant_message.content

            # ---------------------------------
            # Execute requested tools
            # ---------------------------------

            for tool_call in assistant_message.tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                print(f"\n[Agent] Tool requested: {tool_name}")
                print(f"[Agent] Arguments: {arguments}")

                result = self.tool_executor.execute(
                    tool_name=tool_name,
                    arguments=arguments,
                )

                print(f"[Tool] Result: {result}")

                # ---------------------------------
                # Send tool result back to the LLM
                # ---------------------------------

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )