import logging, os, sys

def create_logger(dateFormat: str, filePath: str) -> logging.Logger:
    
    '''For Python robots only. Create a logging object that logs
    information to a file and to the terminal. Also log basic
    info before returning the logger'''

    # Set up two handlers - one for the log file, and one for the terminal
    file = logging.FileHandler(filePath)
    terminal = logging.StreamHandler(sys.stdout)

    # Set up logging configuration, and attach the two handlers
    logging.basicConfig(
        datefmt=dateFormat,
        format='%(asctime)s - %(filename)s - Line %(lineno)d - %(levelname)s - %(message)s\n',
        handlers=[file, terminal],
        level= logging.INFO
    )
    
    # Create logger, log basic info, and return logger
    logger = logging.getLogger(__name__)
    logger.info('Current User: ' + os.environ['USERNAME'])
    logger.info('Machine Name: ' + os.environ['COMPUTERNAME'])
    logger.info('Workspace ID: ' + os.environ['RC_WORKSPACE_ID'])
    return logger