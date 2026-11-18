
from evaluator import analyze_code
from test_evaluator import evaluate_function


# Sample Python code to analyze
code = """
def add_numbers(a, b):
    \"\"\"Add two numbers and return the result.\"\"\"
    return a + b
"""


# Analyze the submitted code
analysis_result = analyze_code(code)

print("CODE ANALYSIS")
print("----------------------")
print("Syntax Valid:", analysis_result["syntax_valid"])
print("Functions:", analysis_result["functions"])
print("Loop Count:", analysis_result["loop_count"])
print("Line Count:", analysis_result["line_count"])
print("Issues:", analysis_result["issues"])
print("Code Quality Suggestions:", analysis_result["quality_issues"])


# Function to test
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b


# Test cases
test_cases = [
    {"input": [2, 3], "expected": 5},
    {"input": [10, 20], "expected": 30},
    {"input": [-2, 5], "expected": 3},
    {"input": [0, 0], "expected": 0}
]


# Evaluate the function
test_result = evaluate_function(add_numbers, test_cases)

print("\nTEST EVALUATION")
print("----------------------")
print("Total Tests:", test_result["total_tests"])
print("Passed:", test_result["passed"])
print("Failed:", test_result["failed"])
print("Pass Percentage:", test_result["pass_percentage"], "%")

print("\nIndividual Test Results:")

for item in test_result["results"]:
    print(item)

