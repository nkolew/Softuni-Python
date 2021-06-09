def is_positive(x):
    return x >= 0


def is_negative(x):
    return x < 0


nums = [int(x) for x in input().split()]

positive_sum = sum(filter(is_positive, nums))
negative_sum = sum(filter(is_negative, nums))

print(negative_sum)
print(positive_sum)

print("The negatives are stronger than the positives" if abs(negative_sum)
      > positive_sum else "The positives are stronger than the negatives")
