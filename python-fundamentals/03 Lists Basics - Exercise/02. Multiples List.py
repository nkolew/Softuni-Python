factor = int(input())
count = int(input())

multiples_list = []

for num in range(1,count+1):
    multiples_list.append(num*factor)

print(multiples_list)

# print([num*factor for num in range(1,count+1)])