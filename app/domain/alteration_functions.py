#general import

#local import
from app.schemas.typing import *

class GeneralterartionFonctions:

    """
    this class of functions is about to work on patterns' atcg sequence.
    they return the the sequence
    """

    def remplace_pattern(sequence: genome, 
                            olde_pattern: str | None=None, 
                            new_pattern :str | None=None, 
                            index_start : str | None=None, 
                            index_end : str | None=None)-> genome:
        """
        remplace a pattern of bases by another one
        Indices can be used if one works with indices rather than replacing each recognized pattern.
        """
        return 
    
    def delete_pattern(sequence: genome, pattern: str, 
                       index_start : str | None=None, 
                       index_end : str | None=None)-> genome:
        """
        delet all patters from a sequence
        Indices can be used if one works with indices rather than replacing each recognized pattern.
        """
        return

    def add_pattern(sequence: genome, pattern: str,
                    index: int | None=None, 
                    left_neighbor_pattern :str | None=None,
                    right_neighbor_pattern :str | None=None)-> genome:
        """
        add a pattern at a specific place in the genome
        Here, you either place the pattern at the beginning or end of a neighbor pattern, 
        or you specify the index where you want to place the desired pattern.

        exemple :
            if :
                sequence = "...atatatatatcggcatatatatatat..."
                pattern = "_NEW_PATTERN_"
                left_n_p = "cg"
                right_n_p = "gc"
            then :
                --> "...atatatatatcg_NEW_PATTERN_gcatatatatatat..."
        """
        return
    def cc_past(sequence: genome,
                     start_cc_index: int,
                     end_cc_index: int,
                     start_past_index: int,
                     end_past_index: int,
                     mode: str="copy")-> genome:
        """
        cut (or copy) and past a sequence
        """

class NewSequenceFonctions:

    """
    creating a sequence from scratch
    """
    def repeat(pattern: str, nbr: int, 
                start_pattern: str="", 
                end_pattern: str="")-> genome:
        """
        repeats a pattern a number of times, with a non-recursive pattern at the beginning and end
        """
        return
    
    def merge(sequensess :list[genome])-> genome:
        """
        return merged sequences
        """
        return

class RandomAlterationFonctions:
    """
    returns randomly mutated atgc sequences following user-defined probability distributions,
    via other functions of the 'ProbaLaws' class.
    """