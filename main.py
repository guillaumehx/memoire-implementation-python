from src import Calculator
import sys

if __name__ == "__main__":
    calculator = Calculator()
    expressions = sys.argv[1:]

    if not expressions:
        print("You should provide one or several expressions")
        sys.exit()

    for expression in expressions:
        print(calculator.compute(expression))