deck = input().split()
shuffles_count = int(input())

left_half = []
right_half = []

for shuffle in range(shuffles_count):

    current_deck = []

    half = len(deck)//2
    left_half = deck[:half]
    right_half = deck[half:]

    for card in range(half):

        current_deck.append(left_half[card])
        current_deck.append(right_half[card])

    deck = current_deck.copy()

print(deck)


# cards = input().split()
# shuffles_count = int(input())
# middle = len(cards)//2

# for _ in range(shuffles_count):

#     current_shuffle = zip(cards[:middle], cards[middle:])

#     cards.clear()
#     for pair in current_shuffle:
#         cards.extend(pair)

# print(cards)
