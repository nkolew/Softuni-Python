def stock_availability(inventory, op, *args):
    
    def delivery(inventory, args):
        for x in args:
            inventory.append(x)
        return inventory

    def sell(inventory, args):
        if args:
            for a in args:
                if isinstance(a, int):
                    for i in range(a):
                        inventory.pop(0)
                elif isinstance(a, str):
                    while a in inventory:
                        inventory.pop(inventory.index(a))
        else:
            inventory.pop(0)
        
        return inventory

    
    ops = {
        'delivery': delivery,
        'sell': sell,
    }

    return ops[op](inventory, args)



# from collections import deque
# from typing import Deque, List


# def stock_availability(inventory_list: List[str], op: str, *args):

#     inventory = deque(inventory_list)

#     def delivery(inventory: Deque[str], *args: str):
#         for a in args:
#             inventory.append(a)

#     def sell(inventory: Deque[str], *args):
#         if not args:
#             inventory.popleft()

#         elif len(args) == 1 and isinstance(args[0], int):
#             a = args[0]
#             for _ in range(a):
#                 inventory.popleft()

#         else:
#             for a in args:
#                 while a in inventory:
#                     inventory.remove(a)

#     ops = {
#         'delivery': delivery,
#         'sell': sell,
#     }

#     ops[op](inventory, *args)

#     return list(inventory)


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
