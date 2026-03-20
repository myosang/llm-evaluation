# Use word match, not semantic analysis.

def correctness(pred, ref):
    return int(ref.lower() in pred.lower())


def grounding(pred, relevant):
    return int(any(p.strip() in pred for p in relevant.split(".")))


def distractor_usage(pred, distractor):
    return int(any(p.strip() in pred for p in distractor.split(".")))


def quality_score(scores):
    return (
        scores["correctness"]
        + scores["grounding"]
        - scores["distractor"]
    )