# imports
from pathlib import Path
import sys
from pipeline.scam_detector.detector import ScamDetector
from utils import get_logger

# path normalization
project_root = Path(__file__).parent
sys.path.append(str(project_root))
logger = get_logger(__name__)


# main function
# calls the scam detection workflow - class
def main():
    """
    Main function that runs the scam detection workflow.
    """

    detector = ScamDetector()
    # test_message = input("Enter the text message to analyze: ")
    test_message = "Congratulations! You've won a free cruise to the Bahamas. Click here to claim your prize."
    try:
        logger.info("Running the scam detection workflow.")
        result = detector.detect(test_message)
        print(f"Input message: {test_message}")
        print(f"Detection result: {result}")
        logger.info("Scam detection completed successfully.")

    except Exception as e:
        logger.error(f"Error during scam detection: {e}")
        print(f"Error during scam detection: {e}")


if __name__ == "__main__":
    main()
