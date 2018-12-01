def multipliers():
    return [lambda x: i * x for i in range(4)]


for m in multipliers():
    print m(2)