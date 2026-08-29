from chatbot_cli.memory import ConversationMemory


def test_initial_history_is_empty():
    memory = ConversationMemory()

    assert memory.get_history() == []

def test_add_message():
    memory = ConversationMemory()

    memory.add_message("user", "こんにちは")
    history = memory.get_history()

    assert len(history) == 1
    assert history[0]["role"] == "user"
    assert history[0]["parts"][0]["text"] == "こんにちは"