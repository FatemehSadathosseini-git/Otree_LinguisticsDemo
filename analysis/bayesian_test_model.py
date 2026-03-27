import argparse
import csv
import random
from pathlib import Path


WORDS = ["circle", "square", "big", "small"]
OBJECTS = ["big circle", "small circle", "big square", "small square"]


def weighted_choice(rng, options, probs):
    x = rng.random()
    c = 0.0
    for option, p in zip(options, probs):
        c += p
        if x <= c:
            return option
    return options[-1]


def make_synthetic_data(n=200, seed=42):
    rng = random.Random(seed)
    word_probs = {
        "big circle": [0.45, 0.05, 0.40, 0.10],
        "small circle": [0.40, 0.05, 0.10, 0.45],
        "big square": [0.05, 0.45, 0.40, 0.10],
        "small square": [0.05, 0.40, 0.10, 0.45],
    }
    word_effect = {"circle": 0.80, "square": 0.80, "big": 0.50, "small": 0.45}
    target_effect = {
        "big circle": 0.10,
        "small circle": 0.00,
        "big square": 0.05,
        "small square": -0.05,
    }

    rows = []
    for _ in range(n):
        target = rng.choice(OBJECTS)
        word = weighted_choice(rng, WORDS, word_probs[target])
        logit = -0.6 + word_effect[word] + target_effect[target]
        p_correct = 1.0 / (1.0 + pow(2.718281828, -logit))
        correct = 1 if rng.random() < p_correct else 0
        if correct:
            guess = target
        else:
            guess = rng.choice([obj for obj in OBJECTS if obj != target])
        rows.append({"target": target, "word": word, "guess": guess, "correct": correct})
    return rows


def load_otree_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            target = row.get("target") or row.get("group.target")
            word = row.get("word") or row.get("player.word")
            guess = row.get("guess") or row.get("player.guess")
            if not target or not word or not guess:
                continue
            rows.append(
                {
                    "target": target,
                    "word": word,
                    "guess": guess,
                    "correct": 1 if guess == target else 0,
                }
            )
    if not rows:
        raise ValueError(
            "No valid rows found. CSV must contain target/word/guess "
            "or group.target/player.word/player.guess."
        )
    return rows


def posterior_summary_binary(successes, failures, samples=10000, seed=42):
    rng = random.Random(seed)
    a = 1 + successes
    b = 1 + failures
    draws = [rng.betavariate(a, b) for _ in range(samples)]
    draws.sort()
    mean = sum(draws) / len(draws)
    low = draws[int(0.025 * len(draws))]
    high = draws[int(0.975 * len(draws))]
    return mean, low, high


def group_posteriors(rows, key):
    counts = {}
    for row in rows:
        k = row[key]
        ok = row["correct"]
        if k not in counts:
            counts[k] = {"success": 0, "failure": 0}
        if ok:
            counts[k]["success"] += 1
        else:
            counts[k]["failure"] += 1
    result = {}
    for k, v in counts.items():
        mean, low, high = posterior_summary_binary(v["success"], v["failure"])
        result[k] = {
            "n": v["success"] + v["failure"],
            "mean": mean,
            "low95": low,
            "high95": high,
        }
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Lightweight Bayesian test model for the oTree reference game"
    )
    parser.add_argument(
        "--csv",
        type=str,
        default="",
        help="Optional path to exported oTree CSV",
    )
    args = parser.parse_args()

    if args.csv:
        csv_path = Path(args.csv)
        if not csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        rows = load_otree_csv(csv_path)
        source = f"oTree CSV: {csv_path}"
    else:
        rows = make_synthetic_data(n=220, seed=42)
        source = "synthetic test data"

    total_correct = sum(r["correct"] for r in rows)
    n = len(rows)
    overall_mean, overall_l, overall_h = posterior_summary_binary(total_correct, n - total_correct)

    print(f"Data source: {source}")
    print(f"Rows used: {n}")
    print(f"Observed accuracy: {total_correct / n:.3f}")
    print(
        "Bayesian overall correctness: "
        f"mean={overall_mean:.3f}, 95% CrI=[{overall_l:.3f}, {overall_h:.3f}]"
    )

    print("\nPosterior by speaker word:")
    by_word = group_posteriors(rows, "word")
    for word in sorted(by_word):
        r = by_word[word]
        print(
            f"  {word:>6} | n={r['n']:>3} | mean={r['mean']:.3f} "
            f"| 95% CrI=[{r['low95']:.3f}, {r['high95']:.3f}]"
        )

    print("\nPosterior by target object:")
    by_target = group_posteriors(rows, "target")
    for target in sorted(by_target):
        r = by_target[target]
        print(
            f"  {target:>12} | n={r['n']:>3} | mean={r['mean']:.3f} "
            f"| 95% CrI=[{r['low95']:.3f}, {r['high95']:.3f}]"
        )


if __name__ == "__main__":
    main()
