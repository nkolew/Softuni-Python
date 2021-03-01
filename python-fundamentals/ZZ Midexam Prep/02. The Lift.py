waiting = int(input())
lift = list(map(int, input().split()))
empty_spots = True

wagon = 0
while True:
    if 0 <= wagon < len(lift):
        if lift[wagon] < 4:
            lift[wagon] += 1
            waiting -= 1
            if not waiting:
                if sum(lift) / 4 == len(lift):
                    empty_spots = False
                break
        else:
            wagon += 1
    else:
        empty_spots = False
        if waiting:
            print(f"There isn't enough space! {waiting} people in a queue!")
        break

if empty_spots:
    print('The lift has empty spots!')

print(" ".join(map(str, lift)))
