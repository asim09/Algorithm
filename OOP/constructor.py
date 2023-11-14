class Point:
    def __new__(cls, *args, **kwargs):
        print('obj created')
        return super().__new__(cls)

    def __init__(self, x, y):
        print('obj initiialized')
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y})"

class const:
    def __init__(self, x):
        self.x = x
        return 43