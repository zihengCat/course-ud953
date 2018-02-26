import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            self.coordinates = tuple(coordinates)
            self.dimension   = len(coordinates)
        except:
            print("Error in init")
    def __str__(self):
        return "Vector: {}".format(self.coordinates)
    def __eq__(self, vector):
        return self.coordinates == vector.coordinates

    def plus(self, vector):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] + vector.coordinates[i])
        return Vector(new_coordinates)
    def minus(self, vector):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] - vector.coordinates[i])
        return Vector(new_coordinates)
    def scalar_mul(self, c):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] * c)
        return Vector(new_coordinates)
    def magnitude(self):
        coordinates_squared = []
        for i in range(len(self.coordinates)):
            coordinates_squared.append(self.coordinates[i] ** 2)
        return math.sqrt(sum(coordinates_squared))
    def normalized(self):
        try:
            magnitudes = self.magnitude()
            return self.scalar_mul(1/magnitudes)
        except:
            print("Error in normalized")

