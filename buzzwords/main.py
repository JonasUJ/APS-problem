import random
from collections import defaultdict

p = 2**63 - 1
a = random.randint(1, p - 1)  

def process_line(line):
    n = len(line)

    hashes = [0] * (n + 1) # Hash prefixes
    multiplier = [1] * (n + 1)

    for i in range(1, n + 1):
        hashes[i] = (hashes[i-1] * a + ord(line[i-1])) % p
        multiplier[i] = (multiplier[i-1] * a) % p

    m = 1 # Word length

    while True:
        frequency_of_hashes = defaultdict(int)

        # rolling hash over remaining string
        for i in range(n - m + 1):
            # Hash of line[i:i+m]
            h = (hashes[i+m] - hashes[i] * multiplier[m]) % p
            frequency_of_hashes[h] += 1

        max_count = max(frequency_of_hashes.values())

        if max_count <= 1:
            print()
            return

        print(max_count)
        m += 1


while True:
    line = input().replace(" ", "")
    if line == "":
        break

    process_line(line)
