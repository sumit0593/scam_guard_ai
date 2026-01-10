from pathlib import Path
from utils import load_file


PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_prompt(filename: str) -> str:
    """
    Docstring for load_prompt

    :param filename: Description
    :type filename: str
    :return: Description
    :rtype: str
    """
    return load_file(PROMPTS_DIR / filename)


PROMPT = load_prompt("react.md")


def generate_prompt(user_input: str) -> str:
    """
    Docstring for generate_prompt

    :param user_input: Description
    :type user_input: str
    :return: Description
    :rtype: str
    """
    template = PROMPT
    return f"{template}\n\nUser Message:\n{user_input.strip()}"
