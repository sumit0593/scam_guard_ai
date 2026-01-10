"""
This file contains main prompt development functionality.
"""

from llm.prompts import generate_prompt

def build_prompt(message: str, strategy: str = "react") -> str:
    """
    Build a prompt for the given user message based on selected strategy.

    Args:
        message: The input message from the user
        strategy: The prompting strategy for the scam detection application
    Returns:
        A formatted prompt ready for LLM consumption
    """
    if strategy == "react":
        return generate_prompt(message)
    else:
        raise NotImplementedError(f"Strategy '{strategy}' is not supported.")
