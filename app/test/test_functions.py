#global import
from functools import wraps

#local import
from app.domain.alteration_functions import PermutationFunctions

# tool test
def print_dic_lisible(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        d = func(*args, **kwargs)

        for muts, genome in d.items():
            print(f"{muts} -> {genome}")

        return d

    return wrapper

seq = "atcgatcg"

window = 4

start, end, step = 0, len(seq), 4

@print_dic_lisible
def f():
    return PermutationFunctions.enumerate_window_mutants(seq, start, end, step, window)

f()
