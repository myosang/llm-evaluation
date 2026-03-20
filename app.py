import gradio as gr
from data import DATASET
from pipeline import run_example, evaluate
import json

def run(idx):
    ex = DATASET[int(idx)]

    # Run both prompts
    output_a, scores_a = run_example("baseline", ex)
    output_b, scores_b = run_example("grounded", ex)

    context = f"""
RELEVANT:
{ex['relevant']}

DISTRACTOR:
{ex['distractor']}
"""

    return (
        ex["question"],
        context.strip(),

        output_a,
        scores_a,

        output_b,
        scores_b,
    )

def build_prompt_board():
    prompts = ["baseline", "grounded"]

    rows = []

    for p in prompts:
        res = evaluate(DATASET, p)
        rows.append([
            p,
            res["quality"],
            res["grounding"],
            res["distractor"],
            res["correctness"]
        ])
    return rows

with gr.Blocks() as app:
    gr.Markdown("# 📊 Response Quality by templates (Observability)")

    board = gr.Dataframe(
        headers=["Prompt", "Quality", "Grounding", "Distractor", "Correctness"],
        value=build_prompt_board()
    )
    refresh_board = gr.Button("Recompute Metrics")

    refresh_board.click(
        fn=build_prompt_board,
        outputs=board
    )

    gr.Markdown("# 🔍 Prompt Comparison Dashboard")
    gr.Markdown("Compare how different prompt templates affect correctness and grounding.")

    idx = gr.Slider(
        minimum=0,
        maximum=len(DATASET) - 1,
        step=1,
        value=0,
        label="Select Example"
    )

    question = gr.Textbox(label="Question", lines=2)
    context = gr.Textbox(label="Context (Relevant + Distractor)", lines=6)

    with gr.Row():
        with gr.Column():
            gr.Markdown("## ❌ Baseline Prompt")
            output_a = gr.Textbox(label="Model Output", lines=5)
            scores_a = gr.JSON(label="Metrics")

        with gr.Column():
            gr.Markdown("## ✅ Grounded Prompt")
            output_b = gr.Textbox(label="Model Output", lines=5)
            scores_b = gr.JSON(label="Metrics")

    # Auto-load initial example
    app.load(
        fn=run,
        inputs=idx,
        outputs=[
            question,
            context,
            output_a,
            scores_a,
            output_b,
            scores_b,
        ],
    )

    # Update when slider changes
    idx.change(
        fn=run,
        inputs=idx,
        outputs=[
            question,
            context,
            output_a,
            scores_a,
            output_b,
            scores_b,
        ],
    )


app.launch()