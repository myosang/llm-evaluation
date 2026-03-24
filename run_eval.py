from data import DATASET
from pipeline import run_example
import numpy as np


def evaluate(dataset, template):
    results = []

    for ex in dataset:
        _, scores = run_example(template, ex)
        results.append(scores)

    return {
        k: np.mean([r[k] for r in results]) # mean of the 3 metrics. 
        for k in results[0]
    }

if __name__ == "__main__":
    for t in ["baseline", "grounded"]:
        print(f"\n{t}")
        print(evaluate(DATASET, t))