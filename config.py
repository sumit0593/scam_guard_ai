import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent
load_dotenv(PROJECT_ROOT / ".env")

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Settings
DEFAULT_MODEL = "gemini-2.5-flash-lite"
MAX_RETRIES = 3
RETRY_DELAY = 2

# Paths
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
LOGS_DIR = PROJECT_ROOT / "logs"



