import dotenv
from google import genai
from loguru import logger


dotenv.load_dotenv()

_client = genai.Client()

def get_response(current_history: list) -> str:

    logger.info("Send a request to Gemini API.")

    response = _client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=current_history,
    )

    logger.info("Received an response from Gemini API successfully.")

    return response.text