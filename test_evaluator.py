
def evaluate_function(function, test_cases):

    results = []
    passed = 0

    for test in test_cases:

        inputs = test["input"]
        expected = test["expected"]

        try:
            actual = function(*inputs)

            if actual == expected:
                status = "Passed"
                passed += 1
            else:
                status = "Failed"

            results.append({
                "input": inputs,
                "expected": expected,
                "actual": actual,
                "status": status
            })

        except Exception as error:

            results.append({
                "input": inputs,
                "expected": expected,
                "actual": str(error),
                "status": "Error"
            })

    total = len(test_cases)

    if total > 0:
        pass_percentage = (passed / total) * 100
    else:
        pass_percentage = 0

    return {
        "total_tests": total,
        "passed": passed,
        "failed": total - passed,
        "pass_percentage": pass_percentage,
        "results": results
    }
