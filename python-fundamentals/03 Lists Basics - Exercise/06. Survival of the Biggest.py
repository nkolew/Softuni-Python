nums_list = [int(num) for num in input().split()]
n = int(input())

for _ in range(n):
    min_num = min(nums_list)
    nums_list.remove(min_num)

print(nums_list)
    