CONTEXTUAL_QUESTION_PROMPT="""Chat History:
-----------------------------
{}
-----------------------------
Follow Up Question: {}

Given the above conversation and a follow up question, rephrase the follow up question to be a standalone question which can be understood without the chat history. Do not add anything from your side, only rephrase the question based on the previous chat history.
Standalone question:"""

ANSWER_PROMPT= """Given context:
-----------------------------
{}
-----------------------------

Question: {}

Given the above context, please answer the user query. Only use the context provided to answer the question.
Answer: """
