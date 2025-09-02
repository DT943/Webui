"""OpenAI client utilities."""

import os
from openai import OpenAI


def get_client() -> OpenAI:
    """Create an OpenAI client using the OPENAI_API_KEY environment variable.

    Returns:
        OpenAI: Configured OpenAI client. If the key is missing, calls
        to the client will fail until a valid API key is provided.
    """
    api_key = os.getenv("OPENAI_API_KEY", "")
    return OpenAI(api_key=api_key)
