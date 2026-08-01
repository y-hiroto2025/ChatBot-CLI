import dotenv
from google import genai
from google.genai import types

# envのロード
dotenv.load_dotenv()

def get_response(user_text, history):
    if history is None: history=[]

    client = genai.Client()

    history.append({"role": "user", "parts": [{"text": user_text}]})

    response = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=history,
    )

    history.append({"role": "model", "parts": [{"text": response.text}]})

    return response.text

# 短期記憶用の会話履歴リスト
history = []

while True:
    text = input("user text: ")
    if text == "0":
        break

    response = get_response(text, history)
    print(f"Gemini: {response}")