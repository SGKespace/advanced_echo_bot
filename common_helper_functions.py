from google.cloud import dialogflow
import os


def detect_intent_texts(text, language_code="ru"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(os.environ["PROJECT_ID"], os.environ["PROJECT_ID"])
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(request={"session": session, "query_input": query_input})

    # return response.query_result.fulfillment_text
    return "" if response.query_result.intent.is_fallback else response.query_result.fulfillment_text