import sys

with open(sys.argv[1]) as input_file:
    priority = 0

    lines = input_file.read().splitlines()

    for i in range(0, len(lines), 3):
        for char in set(iter(lines[i])).intersection(iter(lines[i + 1]), iter(lines[i + 2])):
            if char.islower():
                print(char, 1 + ord(char) - ord("a"))
                priority += 1 + ord(char) - ord("a")
            else:
                print(char, 27 + ord(char) - ord("A"))
                priority += 27 + ord(char) - ord("A")
    print("Priority:", priority)