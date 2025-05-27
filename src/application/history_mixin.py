import json
import os
from datetime import datetime

class HistoryMixin:
    
    def __init__(self, filename="calculator_history.json"):
        self._filename = filename
    
    def add_to_history(self, expression: str, result: float):
        entry = {
            'expression': expression,
            'result': result,
            'timestamp': datetime.now().isoformat()
        }
        history = []
        if os.path.exists(self._filename):
            try:
                with open(self._filename, 'r') as f:
                    history = json.load(f)
            except json.JSONDecodeError:
                history = []
        history.append(entry)
        with open(self._filename, 'w') as f:
            json.dump(history, f, indent = 2)
        
    def get_history(self):
        if not os.path.exists(self._filename):
            return []
        try:
            with open(self._filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    
    def save_history_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.get_history(), f, indent = 2)
    
    def load_history_from_file(self, filename):
        with open(filename, 'r') as f:
            self._history = json.load(f)