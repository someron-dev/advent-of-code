import sys

attacks = ['A', 'B', 'C']

with open(sys.argv[1]) as input_file:
    games = input_file.read().splitlines()

score = 0

for game in games:
    attack = attacks.index(game[0]) + 1
    result = game[2]

    if result == 'Z': # Win
        response = 1 if attack == 3 else attack + 1
        print(attack, response, "Win")
        score += response + 6
    elif result == 'Y': # Draw
        response = attack
        print(attack, response, "Draw")
        score += response + 3
    else: # You Loose
        response = 3 if attack == 1 else attack - 1
        print(attack, response, "Bruh")
        score += response

print("Score:", score)