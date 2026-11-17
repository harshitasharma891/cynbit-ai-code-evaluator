
import ast


def analyze_code(code):
    result = {
        "syntax_valid": False,
        "functions": [],
        "loop_count": 0,
        "issues": []
    }

    # Check whether the submitted code is valid Python
    try:
        tree = ast.parse(code)
        result["syntax_valid"] = True

    except SyntaxError as error:
        result["issues"].append(
            f"Syntax error: {error.msg} at line {error.lineno}"
        )
        return result

    # Look at the different elements in the code
    for item in ast.walk(tree):

        # Find all functions
        if isinstance(item, ast.FunctionDef):
            result["functions"].append(item.name)

        # Count loops
        if isinstance(item, (ast.For, ast.While)):
            result["loop_count"] += 1

    # Add a basic suggestion if no function is defined
    if len(result["functions"]) == 0:
        result["issues"].append(
            "Try using functions to organize your code."
        )

    return result


if __name__ == "__main__":

    sample_code = """
def add_numbers(a, b):
    return a + b
"""

    output = analyze_code(sample_code)

    print("Code Analysis Result")
    print("--------------------")
    print("Syntax Valid:", output["syntax_valid"])
    print("Functions:", output["functions"])
    print("Loops:", output["loop_count"])
    print("Suggestions:", output["issues"])
