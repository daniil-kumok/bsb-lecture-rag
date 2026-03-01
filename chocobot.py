from dotenv import load_dotenv
from mistralai import Mistral
import os


load_dotenv()  # loading api_key and model to be used


def ask_mistral(user_query: str) -> str:
    client = Mistral(api_key=os.getenv("mistral_api_key"))

    chat_response = client.chat.complete(
        model=os.getenv("mistral_llm_model"),
        messages=[
            {
                "role": "user",
                "content": user_query,
            },
        ],
    )

    return chat_response.choices[0].message.content


def answer_question(user_query: str) -> str:
    answer = ask_mistral(user_query)
    return answer


if __name__ == "__main__":
    print(answer_question("hello world"))
