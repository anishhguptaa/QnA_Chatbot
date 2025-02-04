from .prompts import CONTEXTUAL_QUESTION_PROMPT, ANSWER_PROMPT
from openai import OpenAI
client = OpenAI()

def ask_gpt(messages, stream, model="gpt-4o-mini"):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream
    )
    if stream:
        for chunk in completion:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")
        return ""
    else:
        return(completion.choices[0].message.content)


def get_contextual_question(chat_history, question):
    prompt= CONTEXTUAL_QUESTION_PROMPT.format(chat_history, question)
    messages=[
        {
            "role": "system",
            "content": "You are an intelligent AI assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    return ask_gpt(messages=messages, stream=False)

def get_answer(context, question, stream=True):
    prompt= ANSWER_PROMPT.format(context, question)
    
    messages=[
        {
            "role": "system",
            "content": "You are an intelligent assistant to answer user queries related to Ubuntu."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    return ask_gpt(messages=messages, stream=stream)
    
