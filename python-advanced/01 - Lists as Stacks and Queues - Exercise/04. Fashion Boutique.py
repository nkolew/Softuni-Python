clothes = list(map(int, input().split()))
rack_capacity = int(input())

racks = [0]

while clothes:
    current_item = clothes.pop()
    if current_item + racks[-1] > rack_capacity:
        racks.append(current_item)
    else:
        racks[-1] += current_item

print(len(racks))
