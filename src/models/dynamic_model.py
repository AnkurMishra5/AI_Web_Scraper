# Pydantic model generation
from pydantic import BaseModel
from typing import Any

def create_dynamic_model(data: dict):
    """Creates a dynamic Pydantic model based on input data."""
    class DynamicModel(BaseModel):
        __annotations__ = {k: Any for k in data.keys()}

    return DynamicModel(**data)