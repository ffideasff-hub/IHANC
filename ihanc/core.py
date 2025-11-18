# ihanc/core.py
from dataclasses import dataclass, field
from typing import Dict, List, Callable, Any
import datetime
import uuid

@dataclass
class Event:
    id: str
    name: str
    date: datetime.datetime
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class HumanFeedback:
    user: str
    note: str
    weight: float = 1.0

@dataclass
class IARecommendation:
    title: str
    rationale: str
    score: float

class CoopLoop:
    def __init__(self):
        self.events: List[Event] = []
        self.feedback: List[HumanFeedback] = []
        self.recommendations: List[IARecommendation] = []

    def register_event(self, name: str, date: datetime.datetime, **metadata) -> Event:
        ev = Event(id=str(uuid.uuid4()), name=name, date=date, metadata=metadata)
        self.events.append(ev)
        return ev

    def add_feedback(self, fb: HumanFeedback) -> None:
        self.feedback.append(fb)

    def add_recommendation(self, rec: IARecommendation) -> None:
        self.recommendations.append(rec)

    def consensus(self, combine: Callable[[List[HumanFeedback], List[IARecommendation]], Dict[str, Any]]) -> Dict[str, Any]:
        return combine(self.feedback, self.recommendations)
