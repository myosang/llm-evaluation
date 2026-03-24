# 🔍 LLM Prompt Evaluation Dashboard

This project evaluates how different prompt templates affect LLM responses, focusing on **correctness**, **grounding**, and **distractor usage**.

## 🎯 Goal

Compare prompt designs to understand:

- Does the model give the correct answer?
- Does it use the correct part of the context?
- Does it rely on irrelevant (distractor) information?

## ⚙️ Metrics

- **Correctness** → matches reference answer  
- **Grounding** → uses relevant context  
- **Distractor** → uses wrong context  
- **Quality Score**: quality = correctness + grounding - distractor

## 📁 Project Structure

```
llm_evaluation_gradio/
├── data.py          # dataset (question, context, answer)
├──src/
    ├── prompts.py       # prompt templates
    ├── model.py         # OpenAI API call
    ├── metrics.py       # evaluation functions
    ├── pipeline.py      # run + aggregation logic
    ├── run_eval.py      # batch evaluation
    └── app.py           # UI (comparison + dashboard)
```

## 🚀 Setup

Install dependencies:

```
pip install -r requirements.txt
```

## 🧪 Run Evaluation

Run batch evaluation:

```
python3 run_eval.py
```

This prints aggregated metrics per prompt.

## 🖥️ Run UI

Start the dashboard:

```
python3 app.py
```

Open in browser:

```
[http://127.0.0.1:7860](http://127.0.0.1:7860)
```

## 💡 Features

- Side-by-side comparison of prompt outputs  
- Aggregated performance per prompt  
- Detection of incorrect context usage  
- Simple observability of model behavior
  
## 🧠 Key Insight

Prompt design affects not just *what* the model answers, but *whether it uses the correct source of information*.
