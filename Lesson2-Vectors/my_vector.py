import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            self.coordinates = tuple(coordinates)
            self.dimension   = len(coordinates)
        except:
            print("Error format")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)
    def __eq__(self, vector):
        return self.coordinates == vector.coordinates

    # plus: [1, 2] + [3, 4] = [4, 6]
    def plus(self, vector):
        new_coordinates = list()
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] + vector.coordinates[i])
        return Vector(new_coordinates)

    # minus: [4, 3] - [1, 2] = [3, 1]
    def minus(self, vector):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] - vector.coordinates[i])
        return Vector(new_coordinates)

    # scalar_mul: [3, 4] * 2  = [6, 8]
    def scalar_mul(self, c):
        new_coordinates = []
        for i in range(len(self.coordinates)):
            new_coordinates.append(self.coordinates[i] * c)
        return Vector(new_coordinates)

    # magnitude: [3, 4] => sqrt( 3^2 + 4^2 ) = 5
    def magnitude(self):
        coordinates_squared = []
        for i in range(len(self.coordinates)):
            coordinates_squared.append(self.coordinates[i] ** 2)
        return math.sqrt(sum(coordinates_squared))

    # normalized: [3, 4] => 1/5 * [3, 4] = [3/5, 4/5]
    def normalized(self):
        try:
            magnitudes = self.magnitude()
            return self.scalar_mul(1/magnitudes)
        except:
            print("Error when normalized")

