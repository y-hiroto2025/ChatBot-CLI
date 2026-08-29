import json


class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role: str, text: str):
        self.history.append({"role": role, "parts": [{"text": text}]})

    def get_history(self) -> list:
        return self.history

    def save_to_jsonl(self, filepath: str):

        with open(filepath, "a", encoding="utf-8") as f:

            f.write(json.dumps({"event": "session_start"}, ensure_ascii=False) + "\n")
            for message_dict in self.history:
                message_str = json.dumps(message_dict, ensure_ascii=False)
                f.write(message_str + "\n")