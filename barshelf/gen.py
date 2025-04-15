from random import randint

MAX = 1_000_000_000

for i in range(100):
    x, y, z = randint(1, MAX), randint(1, MAX), randint(1, MAX)
    with open(f"test/{i}.gen.in", "w") as fp:
        fp.write(f"1\n{x} {y} {z}")
    with open(f"test/{i}.gen.ans", "w") as fp:
        fp.write("1" if .5 * x >= y >= 2 * z else "0")
