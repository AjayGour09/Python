class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k


v = ThreeDVector(10, 20, 30)

print(v.i)  # 10
print(v.j)  # 20
print(v.k)  # 30