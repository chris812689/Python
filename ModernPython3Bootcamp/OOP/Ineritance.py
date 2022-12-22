class GrumpyDict(dict):
    def __repr__(self):
        print("None of your Business")
        return super().__repr__()
    def __missing__(self, key):
        print(f"You want {key}? Well it ain't here")

data = GrumpyDict({"first": "Tom", "animal": "Cat"})
print(data)