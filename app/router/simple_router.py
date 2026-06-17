#general importation
import traceback
from fastapi import APIRouter

#local importation
from app.schemas.genomic_variants_schema import GeneticVariant
from app.schemas.typing import JSON
from app.services.general_services import ProbaServices, IsValide

router = APIRouter()

@router.post("/GetSimpleProb/")
async def return_simple_proba_json(gv: GeneticVariant):
    """
    return the JSON of proba
    """
    try:
      if IsValide.mutations(gv.mutations) and IsValide.sequence(gv.sequence):
        result= ProbaServices.return_proba_simple(gv)
        return result
    except Exception as e:
      traceback.print_exc()  # print in cmd
      raise
