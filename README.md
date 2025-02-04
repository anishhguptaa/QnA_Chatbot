
# Enterprise QnA Chatbot

Built this QnA chatbot for enterprises with a large volume of documentation files, enabling seamless retrieval of relevant information. The bot employs advanced semantic chunking techniques to break down complex documents and ensure optimal query results. This can be used both as internal tool and also as a 24*7 chatbot for the users. This project features two separate modes::
> FastAPI application
> 
> CLI Application

## Stack used

- OpenAI's `GPT` for LLM and Embeddings.
- `ChromaDB` for vector store.
- `FastAPI` for robust endpoints
## How to use

- Clone the repo

```bash
git clone https://github.com/anishhguptaa/QnA_Chatbot.git
cd QnA_Chatbot
```
<br>

- Install dependencies

```bash
pip install -r requirements.txt
```
<br>

- Create `.env` file. Add `DIRECTORY` which contains all your docs and the `OPENAI_API_KEY`

```bash
cp .env.example .env
```
<br>

- You can either:

<br>

> Start the chatbot via Terminal
> ```bash
> python main.py
> ```
>
> <br>
> 
> Or interact with the FastAPI endpoints via Swagger UI
> ```bash
> python api.py
> ```


## Future scope

- Make a reactive frontend utilising the FastAPI endpoints and the session states.
