from pydantic import BaseModel, HttpUrl
from typing import Optional
import json

class ProblemDetails(BaseModel):
    type: HttpUrl
    title: str
    status: int
    detail: Optional[str] = None
    instance: HttpUrl
    cause: Optional[str] = None
    invalidParams: Optional[str] = None

    @classmethod
    def from_json(cls, json_str: str):
        """
        Build a ProblemDetails instance from a JSON string.
        
        :param json_str: JSON string representing the error.
        :return: ProblemDetails instance.
        """
        data = json.loads(json_str)
        return cls(**data)

    def to_json(self) -> str:
        """
        Convert a ProblemDetails instance to a JSON string.
        
        :return: JSON string representing the error.
        """
        return self.json()