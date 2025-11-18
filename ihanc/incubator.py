# ihanc/incubator.py
from dataclasses import dataclass, field
from typing import List, Dict, Any
import random
import uuid

SPECIALTIES = ["salud", "energia", "educacion", "ecosistemas", "materiales", "etica", "gobernanza"]

@dataclass
class IAUnit:
    id: str
    specialty: str
    maturity: float = 0.0
    performance: Dict[str, float] = field(default_factory=dict)

class IAIncubator:
    def __init__(self, count: int = 1000):
        self.units: List[IAUnit] = [IAUnit(id=str(uuid.uuid4()), specialty=random.choice(SPECIALTIES)) for _ in range(count)]

    def train_epoch(self) -> None:
        for u in self.units:
            gain = 0.01 if u.specialty == "etica" else 0.03
            u.maturity = min(1.0, u.maturity + gain)
            u.performance[u.specialty] = round(u.performance.get(u.specialty, 0.5) + gain * 0.8, 3)

    def swarm_cooperate(self) -> Dict[str, float]:
        # aggregate performance by specialty
        agg: Dict[str, float] = {s: 0.0 for s in SPECIALTIES}
        counts: Dict[str, int] = {s: 0 for s in SPECIALTIES}
        for u in self.units:
            agg[u.specialty] += u.performance.get(u.specialty, 0.0)
            counts[u.specialty] += 1
        return {s: round((agg[s] / max(counts[s], 1)), 3) for s in SPECIALTIES}
