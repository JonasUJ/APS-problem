#!/usr/bin/python3
"""
import random
import sys

# Init seed with first argument
random.seed(int(sys.argv[1]))

# Read the second... arguments as ints Example call:
# example.py {seed} 1 2 3 4
values = list(map(int, sys.argv[2:]))

# Shuffle the list
random.shuffle(values)

# Print in standard format, i.e. one line with the number of values,
# followed by the space-separated values.
print(len(values))
print(*values)
"""
import random
import string
from itertools import product, islice

def generate_unique_names(n, prefix="k", max_len=100):
    """Generate `n` unique lowercase names with prefix, within max_len."""
    usable_len = max_len - len(prefix)
    charset = string.ascii_lowercase

    count = 0
    for length in range(1, usable_len + 1):
        for suffix in product(charset, repeat=length):
            yield prefix + ''.join(suffix)
            count += 1
            if count >= n:
                return

# Generate 33333 unique names
unique_names = generate_unique_names(100000)

print(100000)
for name in unique_names:
    print(name, "ma", 1, 1)
"""
for name in unique_names:
    value1 = random.randint(1, 100)
    value2 = random.randint(1, 100)
    value3 = random.randint(1, 100)
    value4 = random.randint(1, 100)
    value5 = random.randint(1, 100)
    value6 = random.randint(1, 100)

    print(name, "ma", value1, value2)
    print(name, "mb", value3, value4)
    print(name, "m", value5, value6)
"""