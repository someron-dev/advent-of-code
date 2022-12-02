import sys

with open(open(sys.argv[1])) as input_file:
    elves = input_file.read().split("\n\n")
    
    top = 0

    for data in elves:
        total = 0
        for line in data.strip().split("\n"):
            total += int(line)

        if total > top:
            top = total

print("The Elf with the most calories is carrying", top, "cals.")