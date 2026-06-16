#general importation
from dataclasses import dataclass

#local importation
from app.schemas.typing import path

@dataclass
class GlobalVar:
    """
    Contains global variabvles
    """
    CONTEXT: int= 10000
    PATH_FILE_FA: str="" # read
    PATH_FILE_JSON: path="test/proba.json" # write