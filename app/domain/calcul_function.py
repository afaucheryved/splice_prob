#global import
import re

#local import
from app.schemas.typing import *
from app.errors.errors import InvalidMutationSyntax


class IsValid:
    """
    Cheks input syntax.
    """
    def mutations(mutations: list[str]) -> bool:
        for s in mutations:
            """
            verifies a mutation syntaxe
            """
            if not bool(re.match(r"^>p\.\d+\.[atgc]>[atgc]$", s)):
                raise InvalidMutationSyntax(
                    f"Mutation '{s}' does not match syntax: >p.<pos>.<ref>><alt>"
                )
        return True
    
    def sequence(sequence: str) -> bool:
        """
        Verifies the sequence syntaxe
        """
        return bool(re.match(r"^[ACGTacgt]+$", sequence))

class Scoring:
    """
    Calculat score.
    """
    def mut(proba_delta: JSON, norm="euclidian")->float:
        """
        Return a score quantifying the importance of a mutation regarding the change in splicing scores.
        Here, it is the norm of the vector composed of the values from 'proba_json'(acceptor and donor summed in one vector).

        The proposed norms are: 'euclidean' (default), 'eanhattan', and 'quadratic'.
        """
        return