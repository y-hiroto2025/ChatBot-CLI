import dotenv

from chatbot_cli.memory import ConversationMemory
from chatbot_cli.llm import get_response


def main():
    dotenv.load_dotenv()

    memory = ConversationMemory()

    print("---Chat started. Type '0' to exit.---")

    while True:
        user_text = input("User: ")

        if user_text == "0":
            break

        memory.add_message("user", user_text)

        history = memory.get_history()
        response = get_response(history)

        memory.add_message("model", response)

        print(f"Bot: {response}")

    print("---Chat finished.---")


if __name__ == "__main__":
    main()
