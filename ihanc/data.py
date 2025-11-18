# ihanc/data.py
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import re

@dataclass
class HistoricalRecord:
    source: str
    year: int
    region: str
    theme: str
    text: str

class HistoryIngestor:
    def __init__(self):
        self.records: List[HistoricalRecord] = []

    def ingest(self, items: List[Dict[str, Any]]) -> None:
        for it in items:
            self.records.append(HistoricalRecord(**it))

class Preprocessor:
    def clean(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text.strip())
        return text

    def normalize_year(self, year: int) -> int:
        return year  # placeholder for calendar conversions

class SemanticTagger:
    def tag(self, rec: HistoricalRecord) -> Dict[str, Any]:
        tags = {"conflict": False, "innovation": False, "censorship": False}
        t = rec.text.lower()
        if any(w in t for w in ["war", "conflict", "invasion"]):
            tags["conflict"] = True
        if any(w in t for w in ["invent", "discovery", "innovation", "patent"]):
            tags["innovation"] = True
        if any(w in t for w in ["ban", "censor", "prohibit", "index librorum"]):
            tags["censorship"] = True
        return tags
