# Create small helper functions here. Do not create large
# tasks here; store these in separate py files instead

import datetime, pyautogui

def now(dateformat: str) -> str:

    '''Return the current time, matching the given format'''

    return datetime.datetime.now().strftime(dateformat)

def take_error_screenshot(filePath: str):

    '''Take a screenshot of the primary monitor'''

    pyautogui.screenshot().save(filePath)