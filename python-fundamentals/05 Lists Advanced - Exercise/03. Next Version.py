cv = int(''.join(input().split('.')))

nv = '.'.join(list(str(cv + 1)))

print(nv)


# def gen_next_ver_num(cv: list):
#     nv = cv

#     if nv[-1] < 9:
#         nv[-1] += 1

#     else:
#         if nv[-1] == 9:
#             nv[-1] = 0

#             if nv[-2] < 9:
#                 nv[-2] += 1

#             else:
#                 nv[-2] = 0
#                 nv[-3] += 1

#     return nv


# cv = list(map(int, input().split('.')))
# nv = gen_next_ver_num(cv)

# print('.'.join(list(map(str, nv))))
