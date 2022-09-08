# This is the main workflow where all your steps occur.
# Create classes and functions in other py files, and
# import & use them here. This makes your code modular
# and very easy to manage

from libraries.framework import RobotLogging, Utils
from libraries.steps import ExportResults, Login, SubmitForm
from playwright.sync_api import sync_playwright
import yaml

# The first steps of the automation should always be
# creating the config dictionary and the logger
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.loader.BaseLoader)
startTime = Utils.now(config['DateFormat'])
logger = RobotLogging.create_logger(config['DateFormat'],
    config['OutputFolder'] + startTime + '.txt')

try:
    # Start the automation by logging and launching Chromium.
    # Make sure to add headless=False when debugging
    logger.info(config['AutomationName'] + ' automation started')
    browser = sync_playwright().start().chromium.launch()
    page = browser.new_page()
    logger.info(config['LogMessages']['BrowserOpen'])

    # Login to RobotSpareBin
    page = Login.login(config, page)
    logger.info(config['LogMessages']['Login'])
    
    # Submit the RobotSpareBin form
    page = SubmitForm.submit_form(config, page)
    logger.info(config['LogMessages']['Submit'])

    # Export the results to an image file and a PDF file
    page = ExportResults.export_results(config, page)
    logger.info(config['AutomationName'] + ' automation succeeded')

except:
    # Take a screenshot and log the stack trace
    Utils.take_error_screenshot(config['OutputFolder'] +
        startTime + '.png')
    logger.exception(config['LogMessages']['Error'] + '\n')

finally:
    # If there is an active browser, close it before ending
    if browser:
        browser.close()
        logger.info(config['LogMessages']['BrowserClose'])
    logger.info(config['AutomationName'] + ' teardown steps complete')