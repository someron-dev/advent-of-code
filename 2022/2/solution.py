import sys

attacks = ['A', 'B', 'C']
responses = ['X', 'Y', 'Z']

with open(sys.argv[1]) as input_file:
    games = input_file.read().splitlines()

score = 0

for game in games:
    attack = attacks.index(game[0]) + 1
    response = responses.index(game[2]) + 1

    if attack == response: # Tie (3 Points + Response points)
        print(attack, response, "Tie")
        score += 3
    elif response - attack == 1 or response - attack == -2:
        print(attack, response, "Win")
        score += 6
    else: print(attack, response, "Bruh")
    
    score += response

print("Score:", score)