class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point: ({self.x}, {self.y})"
    
    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y))
    
    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))
    
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    

class Vector(Point):
    def __str__(self):
        return f"Vector ({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))
    
p1 = Point(1,1)
p2 = Point(3,1)

v1 = Vector(3,3)
v2 = Vector(5,4)

print(f"Point Class")
print(f"-=-=-=-=-=-=-=-")
print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Point 1 == Point 2?: {p1 == p2}")
print(f"Point 1 + Point 2: {p1 + p2}")
print(f"Distance: {p1.distance(p2)}")
print(f"")
print(f"Vector Class")
print(f"-=-=-=-=-=-=-=-")
print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Vector 1 == Vector 2?: {v1 == v2}")
print(f"Vector 1 + Vector 2: {v1 + v2}")
print(f"Distance: {v1.distance(v2)}")