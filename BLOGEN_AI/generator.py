import os
from dotenv import load_dotenv
from mistralai import Mistral


def genblog(topic: str, api_key: str = None) -> str:
    """
    Generate a unique, plagiarism-free blog post for the given topic.

    Args:
        topic (str): The topic to generate the blog about.

    Returns:
        str: Generated blog content.
    """

    if api_key is None:
        api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError(
            "Please provide your MISTRAL_API_KEY as an argument or set it as an environment variable."
        )

    client = Mistral(api_key=api_key)
    model = "mistral-large-latest"

    response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert content writer. Generate engaging, unique, and plagiarism-free blog posts."},
            {"role": "user", "content": f"Write a detailed blog post about {topic}."}
        ]
    )
    return response.choices[0].message.content
