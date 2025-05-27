from .node_visitor import NodeVisitor
from ..tree.number_node import NumberNode
from ..tree.binary_operation_node import BinaryOperationNode
from ..tree.unary_operation_node import UnaryOperationNode
import math

class EvaluationVisitor(NodeVisitor):

    def visit_number_node(self, node: NumberNode) -> float:
        return node.value

    def visit_binary_operation_node(self, node: BinaryOperationNode) -> float:
        left = node.left.accept(self)
        right = node.right.accept(self)
        op = node.operator
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        elif op == '^':
            return math.pow(left, right)
        else:
            raise ValueError(f"Bad input: {op}")

    def visit_unary_operation_node(self, node: UnaryOperationNode) -> float:
        operand = node.operand.accept(self)
        if node.operator == 'sqrt':
            return math.sqrt(operand)
        else:
            raise ValueError(f"Bad input: {node.operator}")