#!/usr/bin/env python3
"""Generate SYNTHETIC sample answer logs for demonstration.

The data is random, uses fictional brands, and is not a real measurement.
Run it from the repository root.

  python sample-data/generate_sample_data.py
"""
import csv
import random

ENGINES = ["chatgpt", "google-ai-overviews", "gemini", "perplexity", "copilot"]
BRANDS = ["BrightGrid", "NorthWind", "VoltaCore", "ChargeWorks"]
OTHER_SOURCES = ["energyreview.example", "fleetnews.example", "evguide.example",
                 "northwind.example", "voltacore.example", "chargeworks.example",
                 "industrywiki.example", "reviewhub.example"]
BRAND_SOURCE = "brightgrid.example"

PROMPTS = [
    ("P01", "commercial EV charging", "awareness"),
    ("P02", "commercial EV charging", "awareness"),
    ("P03", "commercial EV charging", "consideration"),
    ("P04", "commercial EV charging", "consideration"),
    ("P05", "commercial EV charging", "decision"),
    ("P06", "commercial EV charging", "decision"),
    ("P07", "fleet electrification costs", "awareness"),
    ("P08", "fleet electrification costs", "awareness"),
    ("P09", "fleet electrification costs", "consideration"),
    ("P10", "fleet electrification costs", "consideration"),
    ("P11", "fleet electrification costs", "decision"),
    ("P12", "fleet electrification costs", "decision"),
]

# Probabilities differ between the two runs only to show how the script reports a change.
RUNS = {
    "ai-answer-log-baseline.csv": {"date": "2026-01-12", "brand_mention": 0.30,
                                   "brand_cited": 0.12, "positive": 0.55},
    "ai-answer-log-followup.csv": {"date": "2026-02-23", "brand_mention": 0.46,
                                   "brand_cited": 0.24, "positive": 0.62},
}

FIELDS = ["run_id", "date", "engine", "prompt_id", "topic", "stage",
          "brands_mentioned", "sources_cited", "sentiment", "notes"]


def make_rows(run_name, settings, seed):
    rng = random.Random(seed)
    rows = []
    for engine in ENGINES:
        for prompt_id, topic, stage in PROMPTS:
            mentioned = []
            if rng.random() < settings["brand_mention"]:
                mentioned.append("BrightGrid")
            for rival in BRANDS[1:]:
                if rng.random() < 0.45:
                    mentioned.append(rival)
            sources = rng.sample(OTHER_SOURCES, k=rng.randint(2, 4))
            if rng.random() < settings["brand_cited"]:
                sources.append(BRAND_SOURCE)
            if "BrightGrid" in mentioned:
                sentiment = "positive" if rng.random() < settings["positive"] else "neutral"
            else:
                sentiment = "not_mentioned"
            rows.append({
                "run_id": run_name.replace(".csv", ""),
                "date": settings["date"],
                "engine": engine,
                "prompt_id": prompt_id,
                "topic": topic,
                "stage": stage,
                "brands_mentioned": ";".join(mentioned),
                "sources_cited": ";".join(sources),
                "sentiment": sentiment,
                "notes": "synthetic",
            })
    return rows


def main():
    for index, (name, settings) in enumerate(RUNS.items()):
        path = "sample-data/" + name
        with open(path, "w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(make_rows(name, settings, seed=100 + index))
        print("Wrote", path)


if __name__ == "__main__":
    main()
