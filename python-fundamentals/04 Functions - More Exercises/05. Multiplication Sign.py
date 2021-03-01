def chk_sign(l):

    if all(l):

        negatives = [num for num in l if abs(num) != num]

        if len(negatives) % 2 == 1:
            return 'negative'

        return 'positive'

    return 'zero'


nums = [int(input()) for _ in range(3)]

print(chk_sign(nums))
