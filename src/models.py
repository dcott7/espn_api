from typing import Any, Dict

class ESPNResponse:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
    
    def to_dict(self) -> Dict[str, Any]:
        return self.data

    def __getitem__(self, key: str) -> Any:
        return self.data.get(key)