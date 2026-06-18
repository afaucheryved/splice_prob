#general import

#local import
from app.schemas.typing import *

class ImportanceSplicingSearch:
    """
    Functions that identify the patterns and locations having the greatest impact on splicing probabilities changes.
    Returns a dictionary mapping each position to an importance score regarding the splicing process.
    """

    def zona(sequence: genome,
                threshold: float) -> list[list[int]]:
        """
        It returns, as a list of pairs, the boundaries of the intervals corresponding to regions that significantly impact splicing probabilities (segment/change-point detection), using "ruptures" library.
        To achieve this, the function introduces random mutations every X bases, calculates the delta score, and repeats the process multiple times.
        The results are then combined on a per-base basis and randomized, allowing for the identification of regions where values exceed the threshold.
        """
        return

    def pattern_in_zona(sequence: genome, 
                            zona_intervales: list[list[int]]):
        """
        Uses 'enumerate_window_mutants' followed by 'calcul_y' and 'Scorng.mut', 
        to identify the patterns most significant for altering the splicing score within the previously identified regions of importance.
        """
        return
    