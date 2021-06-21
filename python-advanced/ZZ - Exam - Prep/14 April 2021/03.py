def flights(*args):
    flight_map = {}
    for i in range(0, len(args), 2):
        if args[i] == 'Finish':
            return flight_map
        if args[i] not in flight_map:
            flight_map[args[i]] = 0
        flight_map[args[i]] += int(args[i+1])


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco',
      98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215,
      'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))


# from collections import deque, defaultdict
# from typing import DefaultDict, Deque


# def flights(*args):
#     items: Deque = deque(args)
#     flights_map: DefaultDict[str, int] = defaultdict(int)
#     while True:
#         item = items.popleft()
#         if item == 'Finish':
#             return dict(flights_map)
#         flights_map[item] += int(items.popleft())
