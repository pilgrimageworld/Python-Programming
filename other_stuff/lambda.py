square = lambda x: x * x

# print(square(8))

def apply(fx, value):
    return value * fx(value)

print(apply(lambda x: x*x, 6))