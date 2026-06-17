#general import

#local import
from app.schemas.typing import *

class AlterartionFunctionsByIndex:

    """
    This class of functions is about to work on patterns' atcg sequence.
    They return the new sequence.
    """

    def place_pattern(sequence: genome, 
                            pattern :str, 
                            index :int,
                            lenght :int=0 | str)-> genome:
        """
        Place an actg pattern at an index a over a specified length of the sequence (instead of another one if lenght != 0).
        If 'length' = ":", then the length is the distance from the index to the end of the sequence. 
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
        If 'length' = ":", then the length is the distance from the index to the end of the sequence.
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
    returns randomly mutated atgc sequences following user-defined probability distributions,
    via other functions of the 'ProbaLaws' class.
    """