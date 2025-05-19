# to test: time python3 main.py < long_input.txt > /dev/null

NUM_LINES = 100
CONTENT = "A" * 1000

with open("too_long_input.txt", "w") as f:
    for _ in range(NUM_LINES):
        f.write(CONTENT + "\n")
    f.write("\n")


print(f"Generated file with {NUM_LINES} lines")
