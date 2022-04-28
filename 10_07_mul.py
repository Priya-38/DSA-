class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i +{self.vec[1]}j +{self.vec[2]}k"

    def __mul__(self, vec2):
        sum = 0
        for i in range (len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 7]) 
v2 = Vector([9, 9, 8])   
print(len(v1))
print(len(v2))        