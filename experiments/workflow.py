# imports and setup
# 1. Setup and Config
from google import genai
from google.genai import types
import json
import re
import os
from dotenv import load_dotenv
load_dotenv()

# 2. create client
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_NAME = "gemini-2.5-flash-lite"
# print(GEMINI_API_KEY)
client = genai.Client(api_key=GEMINI_API_KEY)

# 3. create prompt template - ReAct
PROMPT_TEMPLATE = """
You are a highly reliable and safety-focused AI system trained to identify potentially scammy messages.

Follow this exact structured reasoning format:
1. **Thought**: Analyze the tone, urgency, and patterns.
2. **Action**: Classify if this is likely a scam.
3. **Final Answer**: Output a structured JSON.

Return response only in this JSON format:
```
    {{
    "label": "Scam | Not Scam | Uncertain",
    "reasoning": "Your step-by-step analysis",
    "intent": "Sender's intent behind the message",
    "risk_factors": ["List of red flags like urgency, bad links, etc."]
    }}
```
User Message:
{}
"""

# 4. handle input
# user_input = input("Enter the text message to analyze: ")
user_input = "Your package delivery failed. Please update your address at [www.bestwebsite.com] to avoid return to sender."
# print(user_input)

full_prompt = PROMPT_TEMPLATE.format(user_input)
# print(full_prompt)

# 5. generate response with llm
response = client.models.generate_content(
    model=GEMINI_MODEL_NAME,
    contents=full_prompt
)
# print(response.text)

# 6. handle output
def extract_json(text):
    """
    Finds the first '{' and the last '}' in a string 
    and parses it as JSON.
    """
    try:
        # Regex to find the JSON block inside the text
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception as e:
        print(f"JSON Parsing Error: {e}")
    
    # Fallback if parsing fails
    return {
        "label": "Uncertain", 
        "reasoning": "Could not parse AI response",
        "intent": "Unknown",
        "risk_factors": ["Parsing Error"]
    }

parsed_output = extract_json(response.text)
print("="*40)
print(parsed_output)
print(type(parsed_output))
print("="*40)

# print(json.dumps(parsed_output, indent=4))