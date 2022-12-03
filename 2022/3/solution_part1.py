import sys

with open(sys.argv[1]) as input_file:
    priority = 0

    for rucksack in input_file.read().splitlines():
        compartment_len = round(len(rucksack) / 2)

        compartment_1 = set()
        compartment_2 = set()
        for i in range(compartment_len):
            compartment_1.add(rucksack[i])
            compartment_2.add(rucksack[compartment_len + i])

        for char in compartment_1.intersection(compartment_2):
            if char.islower():
                print(char, 1 + ord(char) - ord("a"))
                priority += 1 + ord(char) - ord("a")
            else:
                print(char, 27 + ord(char) - ord("A"))
                priority += 27 + ord(char) - ord("A")
    print("Priority:", priority)