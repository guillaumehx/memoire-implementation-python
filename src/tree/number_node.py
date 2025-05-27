from ast import NodeVisitor
from .expression_node import ExpressionNode

class NumberNode(ExpressionNode):
    
    def __init__(self, value: int):
        self._value = value

    @property
    def value(self) -> int:
        return self._value

    def accept(self, visitor: NodeVisitor) -> float:
        return visitor.visit_number_node(self)

    def __str__(self):
        return f"NumberNode({self._value})"

    def __repr__(self):
        return str(self)