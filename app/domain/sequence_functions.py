#general import
import itertools

#local import
from app.schemas.typing import *
from app.domain.proba_laws_functions import ProbaLawsFunctions
from app.domain.spliceia_calculation import tuple_mutation

class AlterationFunctionsByIndex:

    """
    This class provides functions that operate on ATCG sequences by index.
    They return the new sequence.
    """

    def insert_pattern(sequence: genome,
                            pattern :str, 
                            index :int,
                            length : str | int = 0 )-> genome:
        """
        Place an ATCG pattern at an index over a specified length of the sequence (replacing the existing bases if length != 0).
        If length = ":", then the length is the distance from the index to the end of the sequence. 
        Example:
                pattern = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", length = 16

                                    PLACE (replacing)
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                                    |----------------|
                                   index    (length) |_____
                                    |                      |_____
                                    |                            |____
                                    |aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |
        """
        return 
    
    def delete_pattern(sequence: genome, 
                       start : int, 
                       end : int | None = None,
                       length: int | str | None = None)-> genome:
        """
        DELETEEe the bases beteen the position 'start' and 'end'.
        You can use 'length' parameter instead of 'end'.
        If length = ":", then the length is the distance from the index to the end of the sequence.
        Example:
                        
                                        DELETEEeED
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                                    |----------------|
                                   start  (length)  end
        """
        return

    def move_pattern(sequence: genome, 
                     start_cc: int,
                     end_cc: int,
                     index_paste: int,
                     length_paste: str | int = 0,
                     mode: str = "cut")-> genome:
        """
        Cut (or copy) and paste a sequence.
        Example:
                        
                         CUT                                    PASTE
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                    |-----------|                      |---------------------|
                 start_cc     end_cc               index_paste   (length_past)                                                  
                        

        """
        return

    def copy_pattern(sequence: genome, 
                     start_cc: int,
                     end_cc: int)-> genome:
        """
        Cut (or copy) and paste a sequence.
        Example:
                        
                      COPY / CUT                                PASTE
            -> ...atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg...
                    |-----------|                      |---------------------|
                 start_cc     end_cc               index_paste   (length_past)                                                  
                        

        """
        return

class AlterationFunctionsByPattern:

    """
    This class provides functions that operate on ATCG sequences.
    The entire input sequence is processed by the functions.
    They return the new sequence.
    """

    def replace_pattern(sequence: genome, 
                            old: str, 
                            new: str)-> genome:
        """
        Replace one nucleotide pattern with another.
        ! -> "_" is a wildcard character (matches exactly one ATCG base).
        ! -> "%(n)" is a wildcard character (matches any sequence of up to 'n' ATCG bases).
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
        ! -> "%(n)" is a wildcard character (matches any sequence of up to 'n' ATCG bases).
        Example:

            pattern = "cc_c"
                               DELETEEeE                      DELETEEe
            -> ...atcgatcgatcgatccccgatcgatcgatcgatcgatcgatcctcgatcgatcgatcgatcgatcg...
                                |--|                       |--|
                                                     
                                

        """
        return

class SequenceFactory:

    """
    Functions for generating sequences.
    """
    def repeat(pattern: str, nbr: int, 
                start_pattern: str="", 
                end_pattern: str="")-> genome:
        """
        Repeat a pattern a specified number of times, with optional prefixes and suffixes.
        Example:

            pattern = "atcg", nbr = 10, start_pattern = "aaaa", end_pattern = "cccc"
            
            --> aaaaatcgatcgatcgatcgatcgatcgatcgatcgatcgatcgcccc
            <start> |              <loop>                   | <end>
        """
        return
    
    def merge(sequences: list[genome])-> genome:
        """
        Return the merged sequence.

        Example:

            sequences = ["aaaa", "tttt", "cccc", "gggg"]
            
            --> aaaattttccccgggg
        """
        return

class RandomAlterationFunctions:
    """
    Returns randomly mutated ATCG sequences following user-defined probability distributions,
    using probability distributions defined by the ProbaLawsFunctions class.
    """

    def mutate_independently(sequence: genome, 
                     prob_mat: MutationMatrix
                   )-> genome:
        """
        Apply the mutation probability matrix independently to each base.

        Example:

            If prob_mat[0][1] = 0.01, then an "A" has a 1% chance of becoming a "C".
        """
        return 

class WindowMutationFunctions:

    def enumerate_window_mutants(sequence: genome,
                      start: int, end: int, step: int,
                      window: int = 3, 
                      only_different_bases: bool = True, 
                      max_char: int = 1000000)-> dict[tuple[mut, ...], genome]:
        """
        Returns the dictionary of versions of the sequence
        1: of a specific window position; 
        2: of a version of a possible window mutant of that window.

        Example:

                sequence = "atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg",
                step = 3, start = 0, end = len(sequence)
                window = 4

                so the windows positions [] are, between 'start' and 'end' :
                        ...[atcg][atcg][atcg][atcg]...

                and for each window, the possible window mutants are [gcta], [cctc], etc... such that no base remains at its original position(only_different_bases is True).

                so, a possible version of the sequence is:
                                CHANGE
                        --> atcgatcgatcgatcgatcgatcgatcgatcgatcgatcgatcg
                                |--|
                                gcta

                so, each version of the sequence is entirely defined by a tuple of mutations. In the previous case:
                        --> (">p.5.a>g", ">p.6.t>c", ...)
        Possible improvement: return a `window_mutats` object that stores the base sequence and the set of mutations, and—by design—returns the entire desired mutated sequence upon request.
        """
        
        output: dict[tuple[mut, ...], genome] = {}
        nbr_char = 0

        for i in range(start, end - window +1, step):
            left_seq = sequence[:i]
            seq = sequence[i:i+window]
            right_seq = sequence[i+window:]

            mutant_sequences = itertools.product(seq, repeat=window)

            for p in mutant_sequences:
                perm = "".join(p)
                if (
                    all(seq[k] != perm[k] for k in range(len(perm))) # Ensures that no base remains unchanged at its original position.
                    or (not only_different_bases)
                    ):
                    new_sequence = left_seq + perm + right_seq
                    output[tuple_mutation(old=sequence, new=new_sequence)] = new_sequence
                    vnbr_char+=len(new_sequence)
                    if nbr_char >= max_char:
                        break

        return output