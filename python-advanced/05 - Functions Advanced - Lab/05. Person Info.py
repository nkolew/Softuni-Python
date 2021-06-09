def get_info(**kwargs):
    if 'name' in kwargs and 'town' in kwargs and 'age' in kwargs:
        return f'This is {kwargs["name"]} from {kwargs["town"]} and he is {kwargs["age"]} years old'
