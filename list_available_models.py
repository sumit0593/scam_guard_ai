"""
Script to list all available models from Google Gemini API
"""

from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in environment variables.")
    print("Please ensure you have a .env file with GEMINI_API_KEY set.")
    exit(1)

# Initialize the client
client = genai.Client(api_key=GEMINI_API_KEY)

# List all available models
print("Fetching available models from Google Gemini API...\n")
print("-" * 80)

try:
    models = client.models.list()
    
    print(f"Total Models Available: {len(models)}\n")
    
    for i, model in enumerate(models, 1):
        print(f"{i}. Model: {model.name}")
        print(f"   Display Name: {model.display_name}")
        print(f"   Description: {model.description}")
        print(f"   Input Token Limit: {model.input_token_limit}")
        print(f"   Output Token Limit: {model.output_token_limit}")
        print(f"   Supported Generation Methods: {model.supported_generation_methods}")
        print()
    
    print("-" * 80)
    print(f"\nTotal: {len(models)} models available")

except Exception as e:
    print(f"Error fetching models: {e}")
    exit(1)