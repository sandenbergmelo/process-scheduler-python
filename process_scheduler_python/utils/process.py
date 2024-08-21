from dataclasses import dataclass
from typing import Optional


@dataclass
class Process:
    id: int
    execution_time: float
    priority: Optional[int] = None
    wait_time: float = 0.0
    turn_around_time: float = 0.0
