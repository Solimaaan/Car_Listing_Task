from typing import Dict, TypedDict, Optional, Any

class CarState(TypedDict):
    input: str
    filtered_input: str
    image: Optional[Any]    
    output: Dict[str, Optional[str]]