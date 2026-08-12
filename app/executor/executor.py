import json

from app.tools.registry import TOOL_REGISTRY

class ToolExecutor:
    def execute(self, tool_name:str, arguments:str) -> str:
        '''
        Execute a tool requested by the Agent
        '''

        if tool_name not in TOOL_REGISTRY:
            raise ValueError(
                f"Unknown tool requested: {tool_name}"
            )

        tool = TOOL_REGISTRY[tool_name]

        try:
            parsed_arguments = json.loads(arguments)
            result = tool(**parsed_arguments)

            return str(result)
        
        except Exception as exc:
            return f"Tool execution error: {exc}"

        

