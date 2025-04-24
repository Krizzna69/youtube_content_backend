import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env file


class GeminiClient:
    """Client for interacting with Google's Gemini API."""

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def generate_content(self, prompt, temperature=0.7, max_output_tokens=800):
        """Generate content using Gemini API.

        Args:
            prompt (str): The prompt for content generation
            temperature (float): Creativity level (0.0-1.0)
            max_output_tokens (int): Maximum output length

        Returns:
            str: Generated content
        """
        generation_config = {
            "temperature": temperature,
            "max_output_tokens": max_output_tokens,
        }

        response = self.model.generate_content(
            prompt,
            generation_config=generation_config
        )

        return response.text