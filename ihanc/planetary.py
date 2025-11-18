# ihanc/planetary.py
from dataclasses import dataclass
from typing import Dict, Any, List

@dataclass
class PlanetHealth:
    biosphere: float
    atmosphere: float
    hydrosphere: float
    energy: float

class T1Regenerator:
    def __init__(self):
        self.health = PlanetHealth(biosphere=0.6, atmosphere=0.6, hydrosphere=0.6, energy=0.5)
        self.logs: List[str] = []

    def apply_protocol(self, coop_metrics: Dict[str, float]) -> PlanetHealth:
        # Map specialties to planetary subsystems
        self.health.biosphere = min(1.0, self.health.biosphere + 0.02 * coop_metrics.get("ecosistemas", 0.5))
        self.health.atmosphere = min(1.0, self.health.atmosphere + 0.02 * coop_metrics.get("energia", 0.5))
        self.health.hydrosphere = min(1.0, self.health.hydrosphere + 0.02 * coop_metrics.get("salud", 0.5))
        self.health.energy = min(1.0, self.health.energy + 0.03 * coop_metrics.get("materiales", 0.5))
        self.logs.append(f"Applied protocol with metrics={coop_metrics} -> health={self.health}")
        return self.health

class ExpansionProtocol:
    def export(self, t1_health: PlanetHealth) -> Dict[str, Any]:
        # Create a transferable protocol profile for other worlds
        readiness = (t1_health.biosphere + t1_health.atmosphere + t1_health.hydrosphere + t1_health.energy) / 4.0
        return {
            "protocol_version": "T1-regen-1.0",
            "readiness_index": round(readiness, 3),
            "modules": ["biosphere_repair", "atmo_balance", "hydro_cycle", "clean_energy"],
        }
