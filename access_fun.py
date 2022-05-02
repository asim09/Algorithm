import time

def evaluate_test_cases(test_func, tests):
    test_count = {'TOTAL': 0, 'PASSED': 0, 'FAILED': 0}
    for index, test in enumerate(tests):
        print('=' * 30)
        print()
        print(f"Test Case {index}")

        start = time.time()
        res = test_func(test)
        end = time.time()
        test_count['TOTAL'] = len(tests)

        if res == test['output']:
            test_count['PASSED'] += 1
            print(f"Input {test['input']}, {test['input']['query']}")
            print()
            print(f"Expected Output {test['output']}")
            print()
            print(f"Actual Output {res}")
            print()
            print(f"Runtime of the program is {end - start}")
            print(f"PASSED")
        else:
            test_count['FAILED'] += 1
            print(f"Input {test['input']['cards']}, {test['input']['query']}")
            print()
            print(f"Expected Output {test['output']}")
            print()
            print(f"Actual Output {res}")
            print()
            print(f"Runtime of the program is {end - start}")
            print(f"FAILED")
        print(test_count)