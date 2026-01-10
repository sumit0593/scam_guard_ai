from typing import Dict, Any
from utils import get_logger, extract_json_from_text

logger = get_logger(__name__)


class OutputParser:
    """
    Docstring for OutputParser
    """

    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        """
        Extract and Parse JSON structure from the LLM output.

        Args:
            llm_output: Raw text output from LLM

        Returns:
            Dictionary that contains results from the LLM output
            - label: str -> Classification result (Scam | No Scam | Uncertain),
            - reasoning: str -> Analysis of the classification,
            - intent: str -> Description of the user's intent,
            - risk_factors: List[str] -> List of identified red flags
        """

        logger.info("Parsing LLM output.")

        parsed_json = extract_json_from_text(llm_output)

        if parsed_json:
            logger.info("Successfully parsed LLM output to JSON")
            return parsed_json
        else:
            logger.warning("No JSON found in LLM output")
            fallback_results = {
                "label": "Uncertain",
                "reasoning": "Could not parse AI response",
                "intent": "Unknown",
                "risk_factors": ["Parsing Error"],
            }
            return fallback_results
