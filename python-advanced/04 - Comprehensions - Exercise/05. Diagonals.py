n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
first_dia = [matrix[i][i] for i in range(n)]
second_dia = [matrix[i][n-i-1] for i in range(n)]

print(f'First diagonal: {", ".join(map(str, first_dia))}. Sum: {sum(first_dia)}')
print(f'Second diagonal: {", ".join(map(str, second_dia))}. Sum: {sum(second_dia)}')
