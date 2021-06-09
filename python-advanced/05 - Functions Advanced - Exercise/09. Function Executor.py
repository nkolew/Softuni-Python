def func_executor(*funcs_fargs):
    return [func(*fargs) for func, fargs in funcs_fargs]
