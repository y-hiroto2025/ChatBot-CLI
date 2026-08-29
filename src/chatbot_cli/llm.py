import dotenv
from google import genai


dotenv.load_dotenv()


def get_response(current_history: list) -> str:
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=current_history,
    )

    return response.text
