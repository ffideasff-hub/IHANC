# ihanc/analysis.py
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple
from statistics import mean

@dataclass
class BrakeFactor:
    name: str
    weight: float

class PatternMiner:
    def common_brakes(self, tagged: List[Dict[str, Any]]) -> List[BrakeFactor]:
        counts = {"conflict": 0, "censorship": 0, "inequality": 0, "fragmentation": 0}
        for t in tagged:
            for k in ["conflict", "censorship"]:
                counts[k] += int(t.get(k, False))
        # Simple heuristic weights
        total = sum(counts.values()) or 1
        return [BrakeFactor(n, c / total) for n, c in counts.items()]

class ContrafactualEngine:
    def pivots(self, brakes: List[BrakeFactor]) -> List[Dict[str, Any]]:
        # turn brakes into actionable pivots
        pivots = []
        for bf in brakes:
            if bf.name == "conflict":
                pivots.append({"pivot": "early_mediation_protocols", "impact": bf.weight})
            elif bf.name == "censorship":
                pivots.append({"pivot": "open_knowledge_charter", "impact": bf.weight})
            else:
                pivots.append({"pivot": f"address_{bf.name}", "impact": bf.weight})
        return pivots

class ScenarioGenerator:
    def generate(self, pivots: List[Dict[str, Any]]) -> Dict[str, Any]:
        speed_gain = mean([p["impact"] for p in pivots]) if pivots else 0.0
        return {
            "title": "Accelerated Progress Scenario",
            "pivots": pivots,
            "estimated_tech_acceleration_factor": round(1 + speed_gain, 3),
        }
