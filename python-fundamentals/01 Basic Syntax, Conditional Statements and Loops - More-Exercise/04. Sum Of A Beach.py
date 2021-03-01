word = input()
sum_of_beach = 0

sum_of_beach += word.lower().count('sand')
sum_of_beach += word.lower().count('water')
sum_of_beach += word.lower().count('fish')
sum_of_beach += word.lower().count('sun')

print(sum_of_beach)