from playwright.sync_api import Page
from libraries.framework import WindowsCredentials

def login(config: dict, page: Page) -> Page:
    
    # Request login credentials to log into RobotSpareParts.
    # If this automation is unattended, replace this with
    # code that grabs credentials from Robocorp Vault.

    # In the dialog boxes, enter "maria" for the username
    # and "thoushallnotpass" for the password
    creds = WindowsCredentials.request_credential(
        config['WindowsCredName'])

    # Navigate to the RobotSpareParts site and log in
    page.goto(config['SiteUrl'])
    page.type(config['Selectors']['Username'], creds.username)
    page.type(config['Selectors']['Password'], creds.password)
    page.click(config['Selectors']['Login'])
    
    # Validate successful login by confirming the logout button exists
    page.wait_for_selector(selector=config['Selectors']['Logout'])
    return page
