import gradio as gr
import requests

# Send API requests
API_URL = "http://localhost:8000"

def fetch_example(idx):
    response = requests.get(f"{API_URL}/example/{int(idx)}")
    data = response.json()

    return (
        data["question"],
        data["context"],
        data["baseline"]["output"],
        data["baseline"]["scores"],
        data["grounded"]["output"],
        data["grounded"]["scores"],
    )

def build_prompt_board():
    response = requests.get(f"{API_URL}/leaderboard")
    data = response.json()

    rows = []
    for row in data:
        rows.append([
            row["prompt"],
            row["quality"],
            row["grounding"],
            row["distractor"],
            row["correctness"],
        ])
    return rows

# Build UI
with gr.Blocks() as app:

    gr.Markdown("# 📊 Response Quality by Templates (Observability)")

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
        maximum=10,
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

    # Load initial example
    app.load(
        fn=fetch_example,
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

    # Update on slider change
    idx.change(
        fn=fetch_example,
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

# Run App
if __name__ == "__main__":
    app.launch()