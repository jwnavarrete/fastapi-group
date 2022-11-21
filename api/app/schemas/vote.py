from pydantic import BaseModel
from pydantic.types import conint

class VoteResponse(BaseModel):
    post_id: int
    dir: conint(le=1)