from ast import NodeVisitor
from .expression_node import ExpressionNode

class UnaryOperationNode(ExpressionNode):
    
    def __init__(self, operator: str, operand: ExpressionNode):
        self._operator = operator
        self._operand = operand

    @property
    def operator(self) -> str:
        return self._operator

    @property
    def operand(self) -> ExpressionNode:
        return self._operand

    def accept(self, visitor: NodeVisitor) -> float:
        return visitor.visit_unary_operation_node(self)

    def __str__(self):
        return f"UnaryOperationNode({self._operator}, {self._operand})"

    def __repr__(self):
        return str(self)