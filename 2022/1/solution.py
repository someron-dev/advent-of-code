import sys

with open(sys.argv[1]) as input_file:
    elves = input_file.read().split("\n\n")
    
    all_elves = set()

    for data in elves:
        total = 0
        for line in data.strip().split("\n"):
            total += int(line)

        all_elves.add(total)

sorted_elves = sorted(all_elves)
print("Elve 1:", sorted_elves[-1])
print("Elve 2:", sorted_elves[-2])
print("Elve 3:", sorted_elves[-3])
print(sorted_elves[-3:])
print("Total:", sum(sorted_elves[-3:]))