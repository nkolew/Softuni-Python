n = int(input())

evens = []
odds = []
negatives = []
positives = []

for _ in range(n):

    num = int(input())

    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

num_filter = input()

if num_filter == 'even':
    print(evens)
elif num_filter == 'odd':
    print(odds)
elif num_filter == 'negative':
    print(negatives)
elif num_filter == 'positive':
    print(positives)
