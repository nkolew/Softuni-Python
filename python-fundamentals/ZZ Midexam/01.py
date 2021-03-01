experience_needed = float(input())
battles_count = int(input())
experience = 0
successed = False

for battle in range(1, battles_count+1):
    battle_experience = float(input())
    if battle % 3 == 0:
        battle_experience *= 1.15
        if battle % 5 == 0:
            battle_experience *= 1.05
    if battle % 5 == 0:
        battle_experience *= 0.9

    experience += battle_experience
    if experience >= experience_needed:
        successed = True
        print(
            f'Player successfully collected his needed experience for {battle} battles.')
        break

if not successed:
    print(
        f'Player was not able to collect the needed experience, {experience_needed-experience:.2f} more needed.')
