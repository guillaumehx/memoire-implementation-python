from abc import ABC, abstractmethod

from src.tree.binary_operation_node import BinaryOperationNode
from src.tree.number_node import NumberNode
from src.tree.unary_operation_node import UnaryOperationNode

class NodeVisitor(ABC):

    @abstractmethod
    def visit_number_node(self, node: NumberNode) -> float:
        pass

    @abstractmethod
    def visit_binary_operation_node(self, node: BinaryOperationNode) -> float:
        pass

    @abstractmethod
    def visit_unary_operation_node(self, node: UnaryOperationNode) -> float:
        pass