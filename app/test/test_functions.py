#global import
from functools import wraps

#local import
from app.domain.sequence_functions import WindowMutationFunctions

# tool test
def print_dic_lisible(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        d = func(*args, **kwargs)

        for muts, genome in d.items():
            print(f"{muts} -> {genome}")

        return d

    return wrapper

# var test
seq = "atcgatcg"

window = 4

start, end, step = 0, len(seq), 4

# function test
@print_dic_lisible
def f():
    return WindowMutationFunctions.enumerate_window_mutants(seq, start, end, step, window)

f()
