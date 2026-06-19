#global import
from functools import wraps

#local import
from app.domain.sequence_functions import *

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
seq = "atcgatcgatcgatcgatcg" # 6

window = 4

start, end, step = 0, len(seq), 4

# functions to test

# insert_patter
#delet_pattern
#move_pattern
#copy_past_pattern
#replace pattern
#delete-pattern
# repeat
#merge
# mutate_independently
# enumerate_window_mutants
"""
change : 
index must start at 1 for all functions

"""

#print(AlterationByIndexFunctions.insert_pattern(seq, "NNNN", 1)) # NNNNatcg... # index start 1
#print(AlterationByIndexFunctions.delete_pattern("atcgatcg", 1, 4)) # index start 1
#print(AlterationByIndexFunctions.move_pattern("NNNNatcgatcg", 1, 4, 4)) #index start 1
#print(AlterationByIndexFunctions.copy_past_pattern("NEWPatcgatcg", 1, 4, 4)) # index start 1
#print(AlterationByPatternFunctions.replace_pattern(seq, "atcg", "gcta")) #ok
#print(AlterationByPatternFunctions.delete_pattern(seq, "a")) #ok
#print(SequenceFactory.repeat("atcg", 2)) #ok
#print(SequenceFactory.merge(["atcg", "atcg"])) #ok

