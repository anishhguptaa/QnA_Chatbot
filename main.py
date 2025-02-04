from dotenv import load_dotenv
load_dotenv()

from utils.llm_utils import get_contextual_question, get_answer
from utils.chroma_utils import retrieve_docs, initialise_vector_store

def main():
    chat_history = ""

    print("\nStarting Demo Bot ...")
    initialise_vector_store()
    print("\nStarted Demo Bot")

    while(True):
        if chat_history != "":
            question = input("\n\nQuestion: ")
            chat_history= chat_history + "\nQUESTION: " + question
            question= get_contextual_question(chat_history, question)
            print("Rephrased question: ", question)
        else:
            print("\nStarting new conversation")
            question = input("\n\nQuestion: ")
            chat_history= "QUESTION: " + question
            
        
        context= retrieve_docs(question=question)
        chat_history= chat_history + "\nANSWER: " + question + "\n"
        answer=get_answer(question=question, context=context)

        user_input= input("\n\nStart new, continue or stop? (start/continue/stop): ")
        if(user_input.lower() == "start"):
            chat_history= ""
            continue
        elif(user_input.lower() == "continue"):
            continue
        else:
            print("Exiting Demo Bot!")
            return
        

if __name__ == '__main__':
    main()
