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

            for text_dict in self.history:
                text_str = json.dumps(text_dict, ensure_ascii=False)
                f.write(text_str + "\n")