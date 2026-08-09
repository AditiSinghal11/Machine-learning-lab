LAB 04 - A2
UNIT TESTS FOR BOTH LAB 03 AND LAB 04

These are AI-generated unit tests using ChatGPT.

IMPORTANT:
The same logical test cases are applied to BOTH:
1. Lab 03 original implementations: q2.py, q4.py, ..., q11.py
2. Lab 04 AI-assisted implementations: q2_ai.py, q4_ai.py, ..., q11_ai.py

Each test file contains two test methods:
    test_lab3
    test_lab4_ai

This gives a direct functional comparison under identical test conditions.

FILES:
test_q2_both.py
test_q4_both.py
test_q5_both.py
test_q6_both.py
test_q7_both.py
test_q8_both.py
test_q9_both.py
test_q10_both.py
test_q11_both.py

HOW TO RUN:
Place these test files in the same folder as q*.py and q*_ai.py.

Run one:
    python -m unittest test_q4_both.py

Run all:
    python -m unittest discover

EXPECTED RESULT:
All applicable tests should report PASS/OK.

For the Lab 04 report, include screenshots of the successful
test execution and explain that the same AI-generated unit tests
were applied to both versions for a fair functional comparison.

NOTE:
Some original scripts execute their dataset-loading/printing code
when imported. If an import causes the whole program to execute,
move the executable experiment section under:

    if __name__ == "__main__":

while keeping the function definitions unchanged.
