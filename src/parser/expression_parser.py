from src.tree.expression_node import ExpressionNode
from ..tree.number_node import NumberNode
from ..tree.binary_operation_node import BinaryOperationNode
from .shunting_yard import ShuntingYard
import re

class ExpressionParser:

    def parse(self, expression: str):
        expression = self._preprocess(expression)
        output_queue = ShuntingYard.infixToRPN(expression)
        stack: list[ExpressionNode] = []

        for item in output_queue:
            if isinstance(item, int):
                stack.append(NumberNode(item))
            elif item in ShuntingYard.PRECEDENCE:
                right = stack.pop()
                left = stack.pop()
                stack.append(BinaryOperationNode(item, left, right))

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        return stack.pop()

    def _preprocess(self, expression: str) -> str:
        expression = expression.replace(' ', '')
        expression = re.sub(r'(\d)(\()', r'\1*\2', expression)
        expression = re.sub(r'(\))(\d)', r'\1*\2', expression)
        expression = re.sub(r'(\))(\()', r'\1*\2', expression)
        return expression
