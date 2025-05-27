from abc import ABC, abstractmethod
from ast import NodeVisitor

class ExpressionNode(ABC):

    @abstractmethod
    def accept(self, visitor: NodeVisitor) -> float:
        pass