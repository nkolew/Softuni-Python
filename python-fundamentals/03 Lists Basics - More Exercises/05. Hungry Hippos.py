#####################
# Solution by Pavel #
#####################

def dfs(node, leaps, matrix):

    branch_out = False

    for row in range(node, len(matrix)):
        for col in range(len(matrix[row])):

            if matrix[row][col] == '1':

                if row in range(len(matrix)-1) and col in range(len(matrix[row])-1) \
                        and matrix[row][col+1] == '1' and matrix[row+1][col] == '1':
                    branch_out = True

                if row in range(len(matrix)-1) and matrix[row+1][col] == '1':
                    matrix[row][col] = 0

                elif col in range(len(matrix[row])-1) and matrix[row][col+1] == '1':
                    matrix[row][col] = 0

                else:
                    if not branch_out:
                        leaps += 1

        branch_out = False
        node += 1
        return dfs(node, leaps, matrix)

    return leaps


matrix = [input().split() for idx in range(int(input()))]

print(dfs(0, 0, matrix))
