start = int(input())
end = int(input())

filtered = [n for n in range(start, end+1)
          if any([n % k == 0 for k in range(2, 11)])]

print(filtered)
