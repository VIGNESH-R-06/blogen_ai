import os
from dotenv import load_dotenv
from mistralai import Mistral

# Load environment variables from .env if exists
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError(
        "Please set the MISTRAL_API_KEY in .env file or environment variable.")

model = "mistral-large-latest"
client = Mistral(api_key=api_key)


def blogen(topic: str) -> str:
    """Generate a blog post for a given topic."""
    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert social media content writer."},
            {"role": "user", "content": f"Write a captivating blog post about {topic}."}
        ]
    )
    return response.choices[0].message.content
