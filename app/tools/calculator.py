def calculate(expression: str) -> str:
    '''
    Calculate the Mathematicaly expression.
    This implementation is intentionally simple for learning.
    '''

    try:
        result = eval(expression)
        return str(result)
    except Exception as exc:
        return f"Calculation error: {exc}"


    
