from fastapi import APIRouter
from llm_evaluation_gradio.services.pipeline import evaluate_single, evaluate_dataset
from llm_evaluation_gradio.db.repository import load_dataset
from llm_evaluation_gradio.llm.model import OllamaClient

router = APIRouter()

@router.get("/evaluate/{idx}")
def get_example(idx: int):
    dataset = load_dataset()
    ex = dataset[idx]

    llm = OllamaClient()

    output_a, scores_a = evaluate_single(template="baseline", ex=ex, llm_client=llm)
    output_b, scores_b = evaluate_single(template="grounded", ex=ex, llm_client=llm)

    context = f"""
RELEVANT:
{ex['relevant']}

DISTRACTOR:
{ex['distractor']}
"""

    return {
        "question": ex["question"],
        "context": context.strip(),
        "baseline": {
            "output": output_a,
            "scores": scores_a
        },
        "grounded": {
            "output": output_b,
            "scores": scores_b
        }
    }

@router.get("/leaderboard")
def get_leaderboard():
    dataset = load_dataset()
    llm = OllamaClient()

    prompts = ["baseline", "grounded"]
    rows = []

    for p in prompts:
        res = evaluate_dataset(dataset, p, llm_client=llm)
        rows.append({
            "prompt": p,
            **res
        })

    return rows