# OpenAI integration functions
import openai

def generate_text(prompt, api_key):
    """Generates text using OpenAI's API."""
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response["choices"][0]["text"].strip()