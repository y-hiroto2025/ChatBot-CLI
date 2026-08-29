import dotenv
from loguru import logger

from chatbot_cli.llm import get_response
from chatbot_cli.memory import ConversationSession


def main():
    dotenv.load_dotenv()

    logger.remove()

    logger.add("data/app.log", rotation="1 MB")

    logger.info("Launch a chat application.")

    memory = ConversationSession()
    print("---Chat started. Type '0' to exit.---")

    while True:
        user_text = input("User: ")

        if user_text == "0":

            if memory.get_history() != []:
                memory.save_to_jsonl("data/chat_log.jsonl")
                logger.info("Saved chat logs to JSONL file.")
            break

        memory.add_message("user", user_text)

        history = memory.get_history()
        response = get_response(history)

        memory.add_message("model", response)

        print(f"Bot: {response}")

    print("---Chat finished.---")
    logger.info("Finished a chat application.")


if __name__ == "__main__":
    main()