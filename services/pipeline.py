from llm_evaluation_gradio.llm.model import OllamaClient
from llm_evaluation_gradio.evaluation.prompts import build_prompt
from llm_evaluation_gradio.evaluation.metrics import correctness, grounding, distractor_usage, quality_score
import numpy as np


# Single data instance quality check.
def evaluate_single(template, ex, llm_client):
    prompt = build_prompt(template, ex) # one data instance in dataset is constructed for the given template type.
    output = llm_client.generate(prompt) # generated output is the string of response from model.

    scores = {
        "correctness": correctness(output, ex["answer"]),
        "grounding": grounding(output, ex["relevant"]),
        "distractor": distractor_usage(output, ex["distractor"]),
    }

    scores["quality"] = quality_score(scores)

    return output, scores

# Dataset level quality check
def evaluate_dataset(dataset, template, llm_client):
    results = []

    for ex in dataset:
        _, scores = evaluate_single(template, ex, llm_client)
        results.append(scores)

    return {
        k: round(np.mean([r[k] for r in results]), 3) # mean of the 3 metrics. 
        for k in results[0]
    }
