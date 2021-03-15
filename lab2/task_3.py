import math


class Vector:
    value = []
    dimension = 0

    def __init__(self):
        self.dimension = 0

    def __init__(self, value):
        self.value = value
        self.dimension = self.counter()

    def counter(self):
        i = 0
        for _ in self.value:
            i += 1
        return i

    def get_by_index(self, index):
        count = 0
        for numb in self.value:
            if count == index:
                return numb
            else:
                count += 1

    def check(self, vector):
        self.dimension = self.counter()
        vector.dimension = vector.counter()
        if self.dimension == vector.dimension:
            return True
        else:
            print("Different dimensions")
            return False

    def sum(self, vector):
        if not self.check(vector):
            return self.value
        result_value = []
        for numb_1, numb_2 in zip(self.value, vector.value):
            result_value.append(numb_1 + numb_2)
        return result_value

    def sub(self, vector):
        result_value = []
        for numb_1, numb_2 in zip(self.value, vector.value):
            result_value.append(numb_1 - numb_2)
        return result_value

    def multiply(self, const):
        result_value = []
        for numb in self.value:
            result_value.append(numb * const)
        return result_value

    def multi_scalar(self, vector):
        result = 0
        for numb_1, numb_2 in zip(self.value, vector.value):
            result += numb_1 * numb_2
        return result

    def collinear_vector(self, vector):
        ratio = 0
        for numb_1, numb_2 in zip(self.value, vector.value):
            if numb_1 != 0 and numb_2 != 0:
                ratio = numb_1 / numb_2
                break
        for numb_1, numb_2 in zip(self.value, vector.value):
            if numb_1 != 0 and numb_2 != 0:
                if ratio != numb_1 / numb_2:
                    return False
            else:
                break
        if self.dimension == 3 and vector.dimension == 3:
            if self.get_by_index(1) * vector.get_by_index(2) - self.get_by_index(2) * vector.get_by_index(1) != 0:
                return False
            if self.get_by_index(2) * vector.get_by_index(0) - self.get_by_index(0) * vector.get_by_index(2) != 0:
                return False
            if self.get_by_index(0) * vector.get_by_index(1) - self.get_by_index(1) * vector.get_by_index(0) != 0:
                return False
        return True

    def compare(self, vector):
        if self.dimension != vector.dimension:
            print('different dimensions!!!', self.dimension, vector.dimension)
            return False
        self_length = 0
        for numb in self.value:
            self_length += numb ** 2
        self_length = math.sqrt(self_length)
        vector_length = 0
        for numb in vector.value:
            vector_length += numb ** 2
        vector_length = math.sqrt(vector_length)
        current = 0
        for numb_1, numb_2 in zip(self.value, vector.value):
            current = numb_1 * numb_2
        if self.get_by_index(0) * vector.get_by_index(0) >= 0:
            if self.collinear_vector(vector) and vector_length == self_length:
                return True
        return False

    def print_vector(self):
        print(self.value)

#
# x = Vector()
# y = Vector()
# z = Vector()
#
# x.value = [0, 0, 0]
# x.dimension = x.value.count
# y.value = [0, 2, 3]
# y.dimension = y.value.count
#
# z.value = x.sum(y)
# print('sum = ', z.value)
#
# z.value = x.sub(y)
# print('sub = ', z.value)
#
# z.value = x.multi(5)
# print('multi(5) = ', z.value)
#
# z.value = x.multi_scalar(y)
# print('scalar = ', z.value)
#
# is_similar = x.compare(y)
# print('comparer = ', is_similar)
#
# x.print_vector()

