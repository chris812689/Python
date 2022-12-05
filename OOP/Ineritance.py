class GrumpyDict(dict):
    def __repr__(self):
        print("None of your Business")
        return super().__repr__()

data = GrumpyDict({"first": "Tom", "animal": "Cat"})
print(data)