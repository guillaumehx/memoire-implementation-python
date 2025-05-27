from ..parser.expression_parser import ExpressionParser
from ..visitor.evaluation_visitor import EvaluationVisitor
from .history_mixin import HistoryMixin

class Calculator(HistoryMixin):
    
    def __init__(self):
        super().__init__()
        self._parser = ExpressionParser()
        self._visitor = EvaluationVisitor()

    def compute(self, expression):
        if isinstance(expression, str):
            ast = self._parser.parse(expression)
            result = ast.accept(self._visitor)
            self.add_to_history(expression, result)
            return result
        else:
            result = expression.accept(self._visitor)
            self.add_to_history("expression", result)
            return result
