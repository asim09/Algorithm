
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items
    def is_empty(self):
        return self.items == []
