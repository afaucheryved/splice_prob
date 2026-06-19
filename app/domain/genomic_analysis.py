#general import

#local import
from app.schemas.typing import mut
from app.schemas.typing import *

class ImportanceSplicingSearch:
    """
    Have a function that identify the patterns and locations having the greatest impact on splicing probabilities changes.
    Returns a dictionary mapping each position to an importance score regarding the splicing process.
    """

    @staticmethod
    def _zona(sequence: genome,
                threshold: float, 
                mutation_intensity: int = 10) -> list[list[int]]:
        """
        It returns, as a list of pairs, the boundaries of the intervals corresponding to regions that significantly impact splicing probabilities (segment/change-point detection), using "ruptures" library.
        To achieve this, the function introduces random mutations every N='mutation_intensity' bases, calculates the delta score, and repeats the process multiple times.
        The results are then combined on a per-base basis and randomized, allowing for the identification of regions where values exceed the threshold.
        """
        return

    @staticmethod
    def pattern_in_zona(sequence: genome, 
                            zona_intervales: list[list[int]]) -> dict[set[mut], float] :
        """
        Uses 'enumerate_window_mutants' followed by 'calcul_y' and 'Scoring.mut', 
        to identify the patterns most significant for altering the splicing score within the previously identified regions of importance.
        """
        return
    