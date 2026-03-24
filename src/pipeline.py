from model import generate
from prompts import build_prompt
from metrics import correctness, grounding, distractor_usage, quality_score
import numpy as np


LOG_FILE = "logs.jsonl"

# Single data instance quality check.
def run_example(template, ex):
    prompt = build_prompt(template, ex) # one data instance in dataset is constructed for the given template type.
    output = generate(prompt) # generated output is the string of response from model.

    scores = {
        "correctness": correctness(output, ex["answer"]),
        "grounding": grounding(output, ex["relevant"]),
        "distractor": distractor_usage(output, ex["distractor"]),
    }

    scores["quality"] = quality_score(scores)

    return output, scores

# Dataset level quality check
def evaluate(dataset, template):
    results = []

    for ex in dataset:
        _, scores = run_example(template, ex)
        results.append(scores)

    return {
        k: round(np.mean([r[k] for r in results]), 3) # mean of the 3 metrics. 
        for k in results[0]
    }
