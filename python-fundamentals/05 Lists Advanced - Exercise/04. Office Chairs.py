rooms_count = int(input())
free_chairs = 0
enough_chairs = True

for room in range(1, rooms_count+1):
    chairs, people = input().split()
    chairs = chairs.count('X')
    people = int(people)
    if chairs < people:
        enough_chairs = False
        print(f"{abs(chairs-people)} more chairs needed in room {room}")

    free_chairs += chairs - people

if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
