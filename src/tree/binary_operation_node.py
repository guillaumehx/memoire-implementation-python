from ast import NodeVisitor
from .expression_node import ExpressionNode

class BinaryOperationNode(ExpressionNode):
    
    def __init__(self, operator: str, left: ExpressionNode, right: ExpressionNode):
        self._operator = operator
        self._left = left
        self._right = right

    @property
    def operator(self) -> str:
        return self._operator

    @property
    def left(self) -> ExpressionNode:
        return self._left

    @property
    def right(self) -> ExpressionNode:
        return self._right

    def accept(self, visitor: NodeVisitor) -> float:
        return visitor.visit_binary_operation_node(self)

    def __str__(self):
        return f"BinaryOperationNode({self._operator}, {self._left}, {self._right})"

    def __repr__(self):
        return str(self)