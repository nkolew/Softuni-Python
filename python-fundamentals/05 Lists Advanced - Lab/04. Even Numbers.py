numslist = list(map(int, input().split(', ')))
even_indices = [idx for idx, num in enumerate(numslist) if num % 2 == 0]
print(even_indices)
