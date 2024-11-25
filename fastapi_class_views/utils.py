from fastapi import Request
from pydantic import BaseModel, ValidationError
from typing import Any, Dict

def get_request_data(request: Request) -> Dict[str, Any]:
    """
    Extracts data from the request object.
    
    Args:
        request (Request): The FastAPI request object.
        
    Returns:
        Dict[str, Any]: A dictionary containing the request data.
    """
    # Assuming the request data is in JSON format
    return request.json()

def validate_data(data: Dict[str, Any], schema: BaseModel) -> None:
    """
    Validates request data against a schema.
    
    Args:
        data (Dict[str, Any]): The data to validate.
        schema (BaseModel): The Pydantic model to validate against.
        
    Raises:
        ValidationError: If the data does not conform to the schema.
    """
    try:
        # Validate the data using the provided Pydantic schema
        schema(**data)
    except ValidationError as e:
        # Raise the validation error if data is invalid
        raise e