def age_assignment(*args, **kwargs):
    return {name: val for name in args
            for key, val in kwargs.items()
            if name[0] == key}