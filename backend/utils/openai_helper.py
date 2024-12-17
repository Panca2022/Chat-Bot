import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt: str) -> str:
    try:
        # Generate response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a model like gpt-3.5-turbo or davinci
            prompt=prompt,
            max_tokens=150,  # Adjust token size based on your requirement
            temperature=0.7,  # Adjust creativity of response
            n=1,  # Number of responses
            stop=None  # Optional: define stop sequence
        )

        # Return the generated response text
        return response.choices[0].text.strip()

    except Exception as e:
        return str(e)
