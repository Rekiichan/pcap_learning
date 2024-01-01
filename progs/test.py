import random

random.seed(0)
x = random.choice([1, 2])
random.seed(1)
y = random.choice([1, 2])
print('x', x)
print('y', y)
print(x-y)
