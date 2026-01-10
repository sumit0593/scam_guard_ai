from typing import Optional
from llm.client import LLMClient
from utils import get_logger

logger = get_logger(__name__)


class LLMExecutor:
    """
    Executes prompts using LLM client.
    """

    def __init__(self, model: Optional[str] = None) -> None:
        """
        Initializes the LLMExecutor.

        Args:
            model: Optional argument for specifying model.
        """
        self.llm: LLMClient = LLMClient(model) if model else LLMClient()
        logger.info("Initialized LLMExecutor")

    def execute(self, prompt: str) -> str:
        """
        Executes the prompt using LLM client and returns raw response.

        Args:
            prompt: The formatted prompt string to send to LLM.
        Returns:
            Raw response from LLM.
        Raises:
            Exception: When LLM call fails.
        """
        logger.info(f"Executing LLM with final prompt: {prompt}")
        try:
            response = self.llm.call(prompt)
            logger.info("LLM execution is successful!")

            return response

        except Exception as e:
            logger.error(f"LLM execution failed: {str(e)}")
            raise
