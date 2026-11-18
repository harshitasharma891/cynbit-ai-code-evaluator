# AI-Powered Python Code Evaluation Assistant

## Project Overview

The AI-Powered Python Code Evaluation Assistant is a Python-based prototype designed to analyze Python code and evaluate its output using predefined test cases.

The project checks Python syntax, identifies functions, counts loops, detects basic code quality issues, and evaluates whether a function produces the expected output.

It also provides feedback when a test fails or a runtime error occurs.

## Problem Statement

In coding assessments and learning environments, checking submitted code manually can take time. Learners also need clear feedback to understand why their code is not producing the expected result.

This prototype explores a simple way to automate some parts of Python code evaluation and provide understandable feedback.

## Features

- **Syntax Validation:** Checks whether the submitted Python code has valid syntax.
- **Function Detection:** Identifies function definitions using Python AST.
- **Loop Counting:** Counts `for` and `while` loops.
- **Line Counting:** Counts the lines in the submitted code.
- **Empty Code Detection:** Identifies empty submissions.
- **Code Quality Suggestions:** Detects missing function docstrings and suggests using functions to organize code.
- **Test Case Evaluation:** Compares actual function outputs with expected outputs.
- **Failure Feedback:** Explains the difference between expected and actual results.
- **Runtime Error Handling:** Captures errors such as division by zero.
- **Pass Percentage:** Calculates the percentage of passed test cases.

## Project Structure

```text
cynbit-ai-code-evaluator/
│
├── evaluator.py
├── test_evaluator.py
├── main.py
└── README.md
```

### File Description

| File | Purpose |
|---|---|
| `evaluator.py` | Performs syntax and basic code quality analysis. |
| `test_evaluator.py` | Evaluates test cases and generates feedback. |
| `main.py` | Connects the modules and runs the demonstration. |
| `README.md` | Contains project documentation. |

## Technologies Used

- Python
- Python AST module
- Python functions and exception handling
- Google Colab
- GitHub

## How It Works

1. Python source code is provided to the analyzer.
2. The AST module checks syntax and identifies functions and loops.
3. Basic code quality checks generate suggestions.
4. Predefined test cases are passed to a Python function.
5. Actual results are compared with expected results.
6. The evaluator reports passed tests, failed tests, runtime errors, and pass percentage.

## How to Run

### Requirements

- Python 3
- No external Python packages are required for the current prototype.

### Run the Project

Download the repository files and place them in the same folder.

Open a terminal in that folder and execute:

```bash
python main.py
```

The program will display code analysis and test evaluation results.

The project can also be tested using Google Colab by uploading the three Python files and running:

```python
!python main.py
```

## Testing Results

The prototype was tested using correct and incorrect function implementations.

| Test Scenario | Total Tests | Passed | Failed | Pass Percentage |
|---|---:|---:|---:|---:|
| Correct addition function | 4 | 4 | 0 | 100% |
| Incorrect subtraction function | 4 | 1 | 3 | 25% |
| Division by zero test | 4 | 3 | 1 | 75% |

Additional checks were performed for empty code and missing function docstrings.

## Current Limitations

- The current implementation evaluates predefined Python functions rather than arbitrary student-submitted source code.
- Test cases are manually defined.
- Code quality checks are basic and rule-based.
- The prototype does not currently use an AI/ML model.
- It does not include a secure execution sandbox or a web interface.

## Future Improvements

- Add a secure isolated environment for executing submitted code.
- Support dynamic test case generation.
- Integrate an AI model to explain errors and suggest improvements.
- Add more advanced code quality checks.
- Build a Streamlit-based user interface.
- Generate detailed evaluation reports for each submission.

## Conclusion

This project is an initial prototype for automating Python code analysis and test evaluation. It demonstrates how syntax checking, predefined test cases, and feedback generation can be combined into a single workflow.

The next stage is to extend the prototype with secure code execution and AI-based feedback generation.
