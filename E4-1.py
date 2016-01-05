import random

for i in range(10):
    x = random.random()
    print x




for i in range(10):
    y = random.randint(0, 100)
    print y



t = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']

for i in range(5):
    z = random.choice(t)
    print z
