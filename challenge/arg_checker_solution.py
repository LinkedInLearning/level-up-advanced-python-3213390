from functools import wraps

def arg_checker(*arg_types):
    '''An argument checker decorator that checks both:
    - The number of variables that you use for a function
    - The type of each variable.
    Raises a TypeError if either of these fail''' 
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if len(args) != len(arg_types):
                raise TypeError(f'Function {func.__name__} takes {len(arg_types)} positional arguments but {len(args)} were given')
            for arg, arg_type in zip(args, arg_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f'Function {func.__name__} expected positional arguments of type {arg_type} but got {type(arg)} instead')
            return func(*args)
        return wrapper
    return decorator            