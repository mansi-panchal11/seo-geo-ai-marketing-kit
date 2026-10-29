#!/usr/bin/env python3
"""Compute AI search visibility metrics from a manually logged answer file.

Metrics
  Answer inclusion rate  share of answers that mention the brand
  Share of Voice         brand mentions divided by all tracked brand mentions
  Share of Citation      citations to the brand's domains divided by all citations
  Positive sentiment     share of positive answers among answers that mention the brand

Usage
  python scripts/geo_metrics.py --log sample-data/ai-answer-log-baseline.csv \
      --brand BrightGrid --domains brightgrid.example

  python scripts/geo_metrics.py --log sample-data/ai-answer-log-baseline.csv \
      --compare sample-data/ai-answer-log-followup.csv \
      --brand BrightGrid --domains brightgrid.example --by engine

Standard library only. Python 3.8 or newer.
"""
import argparse
import csv
import sys
from collections import OrderedDict

REQUIRED = ["engine", "prompt_id", "topic", "brands_mentioned", "sources_cited", "sentiment"]
MIN_ANSWERS = 30


def split_list(value):
    """Split a semicolon separated cell into a list of lowercase items."""
    return [item.strip().lower() for item in (value or "").split(";") if item.strip()]


def load_log(path):
    try:
        handle = open(path, newline="", encoding="utf-8")
    except OSError as error:
        sys.exit("Cannot open {}. {}".format(path, error))
    with handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        missing = [name for name in REQUIRED if name not in fields]
        if missing:
            sys.exit("{} is missing the columns {}".format(path, ", ".join(missing)))
        rows = list(reader)
    if not rows:
        sys.exit("{} has no rows".format(path))
    return rows


def percent(part, whole):
    return 100.0 * part / whole if whole else 0.0


def compute(rows, brand, domains):
    brand = brand.lower()
    domains = [d.lower() for d in domains]
    answers = len(rows)
    answers_with_brand = 0
    all_mentions = 0
    brand_mentions = 0
    all_citations = 0
    brand_citations = 0
    positive = 0
    negative = 0

    for row in rows:
        brands = set(split_list(row["brands_mentioned"]))
        all_mentions += len(brands)
        if brand in brands:
            brand_mentions += 1
            answers_with_brand += 1
            sentiment = (row["sentiment"] or "").strip().lower()
            if sentiment == "positive":
                positive += 1
            elif sentiment == "negative":
                negative += 1
        sources = split_list(row["sources_cited"])
        all_citations += len(sources)
        for source in sources:
            if any(source == d or source.endswith("." + d) for d in domains):
                brand_citations += 1

    return OrderedDict([
        ("Answers", answers),
        ("Answer inclusion rate", percent(answers_with_brand, answers)),
        ("Share of Voice", percent(brand_mentions, all_mentions)),
        ("Share of Citation", percent(brand_citations, all_citations)),
        ("Positive sentiment", percent(positive, answers_with_brand)),
    ])


def group_rows(rows, column):
    if column is None:
        return OrderedDict([("All answers", rows)])
    if column not in rows[0]:
        sys.exit("The log has no column named {}".format(column))
    groups = OrderedDict()
    for row in rows:
        groups.setdefault(row[column] or "(blank)", []).append(row)
    return groups


def fmt(name, value):
    return str(value) if name == "Answers" else "{:.1f}%".format(value)


def print_single(groups, brand, domains):
    print("| Group | Answers | Inclusion rate | Share of Voice | Share of Citation | Positive sentiment |")
    print("|---|---|---|---|---|---|")
    for name, rows in groups.items():
        m = compute(rows, brand, domains)
        print("| {} | {} | {} | {} | {} | {} |".format(
            name, m["Answers"], fmt("x", m["Answer inclusion rate"]),
            fmt("x", m["Share of Voice"]), fmt("x", m["Share of Citation"]),
            fmt("x", m["Positive sentiment"])))


def print_compare(before, after, brand, domains):
    print("| Group | Metric | Baseline | Follow-up | Change (points) |")
    print("|---|---|---|---|---|")
    for name in before:
        if name not in after:
            continue
        m1 = compute(before[name], brand, domains)
        m2 = compute(after[name], brand, domains)
        for metric in list(m1.keys())[1:]:
            print("| {} | {} | {} | {} | {:+.1f} |".format(
                name, metric, fmt("x", m1[metric]), fmt("x", m2[metric]), m2[metric] - m1[metric]))


def warn_small(label, rows):
    if len(rows) < MIN_ANSWERS:
        print("Note. {} has only {} answers. Results from fewer than {} answers are unstable.".format(
            label, len(rows), MIN_ANSWERS), file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="AI search visibility metrics from a logged answer file.")
    parser.add_argument("--log", required=True, help="CSV answer log (baseline or single run)")
    parser.add_argument("--compare", help="Second CSV answer log to compare against the first")
    parser.add_argument("--brand", required=True, help="Brand name exactly as written in the log")
    parser.add_argument("--domains", required=True, nargs="+", help="Domains that count as the brand's own sources")
    parser.add_argument("--by", choices=["engine", "topic", "stage"], help="Break results down by this column")
    args = parser.parse_args()

    first = load_log(args.log)
    warn_small(args.log, first)
    groups_first = group_rows(first, args.by)

    if args.compare:
        second = load_log(args.compare)
        warn_small(args.compare, second)
        print_compare(groups_first, group_rows(second, args.by), args.brand, args.domains)
    else:
        print_single(groups_first, args.brand, args.domains)


if __name__ == "__main__":
    main()
