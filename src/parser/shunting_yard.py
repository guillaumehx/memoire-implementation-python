import re

class ShuntingYard:

    PRECEDENCE = { '+': 1, '-': 1, '*': 2, '/': 2, '^': 4 }

    @staticmethod
    def infixToRPN(expression: str) -> list:
        output_queue = []
        operator_stack = []

        tokens = re.findall(r'\d+|\+|\-|\*|\/|\^|\(|\)', expression)

        for token in tokens:
            if token.isdigit():
                output_queue.append(int(token))
            elif token in ShuntingYard.PRECEDENCE:
                while (operator_stack and operator_stack[-1] != '(' and
                       (ShuntingYard.PRECEDENCE[operator_stack[-1]] > ShuntingYard.PRECEDENCE[token] or
                        (ShuntingYard.PRECEDENCE[operator_stack[-1]] == ShuntingYard.PRECEDENCE[token] and token != '^'))):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return output_queue