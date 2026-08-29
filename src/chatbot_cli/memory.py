class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role: str, text: str):
        self.history.append({"role": role, "parts": [{"text": text}]})

    def get_history(self) -> list:
        return self.history
