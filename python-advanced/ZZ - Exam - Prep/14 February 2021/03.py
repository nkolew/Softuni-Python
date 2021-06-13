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
