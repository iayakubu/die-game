import random

max_roll = 5
current_outcome = 0
max_outcome = 20

print("WELCOME TO ROLL THE DIE ...\n\n")
for i in range(1, 6):
    die_roll = random.randint(1, 6)
    current_outcome = current_outcome + die_roll

    print(f"Roll #{i}: You've rolled a {die_roll}")

    if current_outcome == max_outcome:
        print("fYour total outcom is {current_roll}. Congratulations, you win!")
        break
    elif current_outcome > max_outcome:
        print(f"Unfortunately, that takes you past total number of {max_outcome} outcomes, You lose!")
        break
    elif i == max_roll and current_outcome < max_outcome:
        print(f"Your total outcome is {current_outcome}")
        print(f"Unfortunatly, you didn't make it to the total outcomes of {max_outcome} as required. You lose!")
    else:
        remaining_outcomes = max_outcome - current_outcome
        print(f"Your total number of outcomes are {current_outcome}. You still have {remaining_outcomes} to go.")

    print(" \n\n")


