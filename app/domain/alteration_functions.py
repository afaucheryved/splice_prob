#general import
import itertools

#local import
from app.schemas.typing import *
from app.domain.proba_laws_functions import ProbaLawsFunctions
from app.domain.genomic_calculation import tuple_mutation

class AlterartionFunctionsByIndex:

    """
    This class of functions is about to work on patterns' atcg sequence.
    They return the new sequence.
    """

    def place_pattern(sequence: genome, 
                            pattern :str, 
                            index :int,
                            lenght : str | int=0 )-> genome:
        """
        Place an actg pattern at an index a over a specified length of the sequence (instead of another one if lenght != 0).
        If length = ":", then the length is the distance from the index to the end of the sequence. 
        Example:
                pattern = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", lenght = 16

                                    PLACE (instead of)
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                                    |----------------|
                                   index    (lenght) |_____
                                    |                      |_____
                                    |                            |____
                                    |aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
        """
        return 
    
    def delete_pattern(sequence: genome, 
                       start : int, 
                       end : int | None=None,
                       lenght: int | str | None=None)-> genome:
        """
        Delet the bases beteen the position 'start' and 'end'.
        You can use 'lenght' parametter instead of 'end'.
        If length = ":", then the length is the distance from the index to the end of the sequence.
        Example:
                        
                                        DELETED
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                                    |----------------|
                                   start  (lenght)  end
        """
        return

    def cc_past(sequence: genome,
                     start_cc: int,
                     end_cc: int,
                     index_past: int,
                     lenght_past: int=0,
                     mode: str="cut")-> genome:
        """
        Cut (or copy) and past a sequence.
        Example:
                        
                      COPY / CUT                                PAST
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                    |-----------|                      |---------------------|
                 start_cc     end_cc               index_past   (lenght_past)                                                  
                        

        """
        return

class AlterartionFunctionsByPattern:

    """
    This class of functions is about to work on patterns' atcg sequence.
    The entire input sequence is processed by the functions.
    They return the new sequence.
    """

    def replace_pattern(sequence: genome, 
                            olde: str, 
                            new:str, )-> genome:
        """
        Replace a pattern of bases by another one
        ! -> "_" is a wildcard character (replaces 1 atcg base).
        ! -> "%(n)" is a wildcard character (replaces any long sequence of up to 'n' ATCG bases).
        Example:

            old = "cc_c", new = "aaaa"
                               REPLACE                  REPLACE
            -> ...atcgatcgatcgatccccgatcgatcgatcgatcgatcgatcctcgatcgatcgatcgatcgatcg...
                                |--|                       |--|
                                aaaa                       aaaa
                                

        """
        return 
    
    def delete_pattern(sequence: genome, 
                       pattern: str, 
                       )-> genome:
        """
        ! -> "_" is a wildcard character (replaces 1 atcg base).
        ! -> "%(n)" is a wildcard character (replaces any long sequence of up to 'n' ATCG bases).
        Example:

            pattern = "cc_c"
                               DELETE                      DELET
            -> ...atcgatcgatcgatccccgatcgatcgatcgatcgatcgatcctcgatcgatcgatcgatcgatcg...
                                |--|                       |--|
                                aaaa                       aaaa
                                

        """
        return

class NewSequenceFunctions:

    """
    Generating a sequence.
    """
    def repeat(pattern: str, nbr: int, 
                start_pattern: str="", 
                end_pattern: str="")-> genome:
        """
        Repeats a pattern a number of times, with a non-recursive pattern at the beginning and end.
        Example:

            pattern = "atcg", nbr = 10, start_pattern = "aaaa", end_attern = "cccc"
            
            --> aaaaatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgcccc
            <start> |              <lopp>                   | <end>
        """
        return
    
    def merge(sequenses :list[genome])-> genome:
        """
        Return merged sequences.

        Example:

            sequences = ["aaaa", "tttt", "cccc", "gggg"]
            
            --> aaaattttccccgggg
        """
        return

class RandomAlterationFonctions:
    """
    Returns randomly mutated atgc sequences following user-defined probability distributions,
    via other functions of the 'ProbaLaws' class.
    """

    def base_by_base(sequence: genome, 
                     prob_mat: MutationMatrix
                   )-> genome:
        """
        applies a probability law to each basis, which causes it to mutate or not depending on the probability matrix

        Example:

            If proba_mat[0][1] = 0.01, so a "a" have 1% chance to become a "c"
        """
        return 

class PermutationFunctions:

    def permutations(sequence: genome, 
                      start: int, end: int, step: int,
                      window: int=3, 
                      only_different_bases: bool=True)-> dict[tuple[mut, ...], genome]:
        """
        Returns the dictionary of versions of the sequence, each containing a permutation: 
        1: of a specific window position; 
        2: of a version of a possible permutation of that window.

        Example:

                sequence = "atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg",
                step = 3, start = 0, end = len(sequence)
                window = 4

                so the windows positions [] are, between 'start' and 'end' :
                        ...[atcg][atcg][atcg][atcg]...

                and for each  window, the possibles permutations are [gcta], [cctc], etc... without a base in the same location as the original sequence (only_different_bases is True).

                so, a possible version of sequence is:
                                CHANGE
                        --> atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg
                                |--|
                                gcta

                so, each versions of the sequence is enterely defines by a tuple of mutations. In the previous cas:
                        --> (">p.5.a>t", ">p.6.t>c", ...)
        """
        
        output: dict[tuple[mut, ...], genome] = {}

        for i in range(start, end - window +1, step):
            left_seq = "".join([sequence[k] for k in range(i)])
            seq = "".join([sequence[k] for k in range(i, i+window)])
            right_seq = "".join([sequence[k] for k in range(i+window, len(seq)-1)])

            permutations_seq = itertools.product(seq, repeat=window)

            for p in permutations_seq:
                perm = "".join(p)
                if (
                    all(seq[k] != perm[k] for k in range(len(perm))) # Checks if any bases are similar to those in the original sequence at the same location.
                    or (not only_different_bases)
                    ):
                    output[tuple_mutation(old=seq, new=perm)] = left_seq + perm + right_seq

        return output