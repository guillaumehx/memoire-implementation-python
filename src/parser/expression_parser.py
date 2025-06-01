from src.tree.expression_node import ExpressionNode
from ..tree.number_node import NumberNode
from ..tree.binary_operation_node import BinaryOperationNode
from .shunting_yard import ShuntingYard

class ExpressionParser:

    def parse(self, expression: str):
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