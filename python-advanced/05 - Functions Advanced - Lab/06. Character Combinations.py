def print_comb(text, idx):
    if idx >= len(text):
        print(''.join(text))
        return
    print_comb(text, idx+1)
    for i in range(idx+1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        print_comb(text, idx+1)
        text[idx], text[i] = text[i], text[idx]


text = list(input())
print_comb(text, 0)


# ##################
#
#  HEAP'S ALGORITHM
#
# ##################
#
# permutations = set()

# def generate(k, A):
#     if k == 1:
#         permutations.add(''.join(A))
#     else:
#         generate(k-1, A)
#         for i in range(0, k-1):
#             if k % 2 == 1:
#                 A[i], A[k-1] = A[k-1], A[i]
#             else:
#                 A[0], A[k-1] = A[k-1], A[0]
#             generate(k - 1, A)


# l = list(input())

# generate(len(l), l)
# print('\n'.join(list(permutations)))
