# main.py
import datetime
from ihanc.core import CoopLoop, HumanFeedback, IARecommendation
from ihanc.data import HistoryIngestor, Preprocessor, SemanticTagger
from ihanc.analysis import PatternMiner, ContrafactualEngine, ScenarioGenerator
from ihanc.incubator import IAIncubator
from ihanc.planetary import T1Regenerator, ExpansionProtocol

def demo():
    # 1) History as data
    ingest = HistoryIngestor()
    ingest.ingest([
        {"source": "Chronicle A", "year": 1540, "region": "EU", "theme": "science", "text": "Censorship slowed knowledge transfer."},
        {"source": "Archive B", "year": 1914, "region": "EU", "theme": "politics", "text": "War disrupted innovation and collaboration."},
        {"source": "Record C", "year": 1965, "region": "Global", "theme": "tech", "text": "Discovery and innovation flourished with open collaboration."},
    ])
    prep = Preprocessor()
    tagger = SemanticTagger()
    tagged = []
    for r in ingest.records:
        r.text = prep.clean(r.text)
        tagged.append(tagger.tag(r))

    # 2) Contrafactual analysis
    miner = PatternMiner()
    brakes = miner.common_brakes(tagged)
    engine = ContrafactualEngine()
    pivots = engine.pivots(brakes)
    scenario = ScenarioGenerator().generate(pivots)

    # 3) Implementation event
    loop = CoopLoop()
    loop.add_feedback(HumanFeedback(user="ONU-Panel", note="Priorizar datos abiertos y mediación temprana", weight=1.2))
    loop.add_recommendation(IARecommendation(title="Open Knowledge Charter", rationale="Reduce censura estructural", score=0.9))
    event = loop.register_event("Cumbre Mundial H+IA", datetime.datetime(2030, 1, 1), manifesto="Cooperación planetaria", scenario=scenario)
    consensus = loop.consensus(lambda fb, rec: {
        "avg_weight": sum(f.weight for f in fb) / max(len(fb), 1),
        "avg_score": sum(r.score for r in rec) / max(len(rec), 1),
    })

    # 4) IA incubator
    incubator = IAIncubator(count=5000)  # millions in production, thousands in demo
    for _ in range(10):
        incubator.train_epoch()
    coop_metrics = incubator.swarm_cooperate()

    # 5) T1 planetary regeneration
    t1 = T1Regenerator()
    health = t1.apply_protocol(coop_metrics)

    # 6) Export protocol to future worlds
    protocol = ExpansionProtocol().export(health)

    # Print a concise report
    print("=== IHANC Demo Report ===")
    print(f"Event: {event.name} on {event.date.date()}")
    print(f"Scenario: {scenario['title']} | Acceleration factor: {scenario['estimated_tech_acceleration_factor']}")
    print(f"Consensus: {consensus}")
    print(f"Incubator coop metrics: {coop_metrics}")
    print(f"T1 Health: biosphere={health.biosphere:.3f} atmosphere={health.atmosphere:.3f} hydrosphere={health.hydrosphere:.3f} energy={health.energy:.3f}")
    print(f"Exported Protocol: {protocol}")

if __name__ == "__main__":
    demo()
