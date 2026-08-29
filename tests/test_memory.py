from chatbot_cli.memory import ConversationSession


def test_initial_history_is_empty():
    memory = ConversationSession()

    assert memory.get_history() == []

def test_add_message():
    memory = ConversationSession()

    memory.add_message("user", "こんにちは")
    messages = memory.get_history()

    assert len(messages) == 1
    assert messages[0]["role"] == "user"
    assert messages[0]["parts"][0]["text"] == "こんにちは"