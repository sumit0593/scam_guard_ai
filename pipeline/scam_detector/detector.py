# imports
from typing import List, Dict, Any
from .executor import LLMExecutor
from .parser import OutputParser
from .builder import build_prompt
from utils import get_logger

# logger
logger = get_logger(__name__)

# scam detection class
class ScamDetector:
    """
    Docstring for ScamDetector
    """

    def __init__(self, strategy: str = "react") -> None:
        """
        Initialized the scam detection pipeline.
        """
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Initialized ScamDetector with strategy -> {self.strategy}")

    def detect(self, message: str) -> Dict[str, Any]:
        """
        Runs the main scam detection pipeline.
        """
        logger.info(f"Started detection for input message")
        try:
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)
            
            logger.info(f"Detection successful!")
            return parsed_result

        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")