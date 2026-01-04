from google import genai
from google.genai import types
from pydantic import BaseModel
import os
from dotenv import load_dotenv  # Import this

# Load environment variables from the .env file
load_dotenv()

# --- API KEY CONFIGURATION ---


# 1. Get the API Key
api_key = os.environ.get("GEMINI_API_KEY")

# Optional: Get model from env, or default to a string
model_name = os.environ.get("model", "gemini-2.0-flash-exp")

# Debug print (you can remove this later)
print(f"Debug - Key found: {'Yes' if api_key else 'No'}")
print(f"Debug - Model: {model_name}")

if not api_key:
    print("Error: API Key not found. Check your .env file.")


def load_system_prompt(filename="prompt.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f"Debug - Loaded system prompt from {filename}")
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return "You are a helpful assistant."  # Fallback prompt


prompt = load_system_prompt()
