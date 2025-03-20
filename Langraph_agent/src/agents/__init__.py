from typing import Dict, Any, Protocol

class Agent(Protocol):
    def __call__(self, state: Dict[str, Any]) -> Dict[str, Any]:
        ...