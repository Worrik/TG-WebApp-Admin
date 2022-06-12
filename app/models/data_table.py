from typing import Dict, List, Optional
from pydantic import BaseModel

from app.models.config import Header


class DataTable(BaseModel):
    """
    DataTable class
    """
    totalItems: int
    items: List[Dict]
    headers: List[Header]
    loading: Optional[bool] = True

