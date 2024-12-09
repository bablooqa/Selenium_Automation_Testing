import logging
import allure

# Configure logging
logging.basicConfig(
    filename='logs/test_log.log',  # Specify log file location
    filemode='a',  # Append mode, so old logs won't be overwritten
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
    level=logging.INFO  # Set minimum logging level (INFO, DEBUG, ERROR, etc.)
)

# Create a logger
logger = logging.getLogger(__name__)

# Define a function to log messages and add them to Allure reports
def allure_log(message, *args):
    logger.info(message, *args)  # Log the message to the file
    formatted_message = message % args if args else message
    allure.attach(
        formatted_message, name="Log Message", attachment_type=allure.attachment_type.TEXT
    )
