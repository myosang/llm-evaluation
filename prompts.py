def build_prompt(template, ex):
    context = ex["relevant"] + "\n" + ex["distractor"]

    # Verify the correctness of the answer to the question.
    if template == "baseline":
        return f"""
        Answer the question:

        {ex['question']}

        Context:
        {context}
        """
    # Verify if the answer comes from the relevant context, not distractor.
    elif template == "grounded":
        return f"""
        Answer using ONLY the provided context.
        If unsure, say "I don't know".

        Question: {ex['question']}

        Context:
        {context}
        """
