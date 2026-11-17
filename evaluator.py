
import ast


def analyze_code(code):

    result = {
        "syntax_valid": False,
        "functions": [],
        "loop_count": 0,
        "line_count": 0,
        "issues": [],
        "quality_issues": []
    }

    # Check whether code is empty
    if not code.strip():
        result["issues"].append("Code is empty.")
        return result

    result["line_count"] = len(code.splitlines())

    # Check Python syntax
    try:
        tree = ast.parse(code)
        result["syntax_valid"] = True

    except SyntaxError as error:
        result["issues"].append(
            f"Syntax error: {error.msg} at line {error.lineno}"
        )
        return result

    # Check functions and loops
    for item in ast.walk(tree):

        if isinstance(item, ast.FunctionDef):
            result["functions"].append(item.name)

            if ast.get_docstring(item) is None:
                result["quality_issues"].append(
                    f"Function '{item.name}' is missing a docstring."
                )

        if isinstance(item, (ast.For, ast.While)):
            result["loop_count"] += 1

    # Give basic code improvement suggestions
    if len(result["functions"]) == 0:
        result["quality_issues"].append(
            "Consider using functions to organize your code."
        )

    return result
