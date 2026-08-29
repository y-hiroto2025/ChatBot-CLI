import json
from typing import Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    role: Literal["user", "model"]
    text: str

    def to_gemini_format(self) -> dict:
        return {"role": self.role, "parts": [{"text": self.text}]}

class ConversationSession(BaseModel):
    messages: list[Message] = Field(default_factory=list)

    def add_message(self, role: str, text: str):
        self.messages.append(Message(role=role, text=text))

    def get_history(self) -> list[dict]:
        return [msg.to_gemini_format() for msg in self.messages]

    def save_to_jsonl(self, filepath: str):

        with open(filepath, "a", encoding="utf-8") as f:

            f.write(json.dumps({"event": "session_start"}, ensure_ascii=False) + "\n")
            for msg in self.messages:
                text_str = json.dumps(msg.model_dump(), ensure_ascii=False)
                f.write(text_str + "\n")