class Point:
    def __init__(self, x: int = 0, y: int =0):
        self._x = x
        self._y = y

    def distance(self, point) -> int:
        if isinstance(point, Point):
            dx = self.x - point.x
            dy = self.y - point.y
        return (dx**2 + dy**2)**0.5
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y
