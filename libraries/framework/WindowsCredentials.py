# For attended automations only. Uses RPA.Dialogs to request credentials from
# users, and keyring to store & retrieve them with Windows Credential Manager

from RPA.Dialogs import Dialogs
import keyring
dialogs = Dialogs()

def windows_request_credential(credName: str) -> keyring.core.credentials.Credential:

    '''For attended automations only. Request credentials from users to be
    used later in the automation, and returns a SimpleCredential object

    https://keyring.readthedocs.io/en/latest/#keyring.credentials.SimpleCredential'''

    # If the credential exists already, ask the user if
    # they want to update their username and password
    cred = keyring.get_credential(credName, None)
    update = 'Yes'
    if cred:
        dialogs.add_heading('Update existing credentials?')
        dialogs.add_radio_buttons('update', ['Yes','No'])
        update = dialogs.run_dialog(title='Robocorp Dialog', height=330, on_top=True)['update']
    
    # If the user said they want to update, or if the credential
    # does not exist, have the user enter their username and
    # password and store it in Windows Credential Manager
    if update == 'Yes':
        dialogs.add_heading('Enter new credentials:')
        dialogs.add_text_input('user', 'Username')
        dialogs.add_password_input('pass', 'Password')
        output = dialogs.run_dialog(title='Robocorp Dialog', height=370, on_top=True)
        if cred:
            keyring.delete_password(credName, cred.username)
        keyring.set_password(credName, output['user'], output['pass'])
    
    # Use the properties .username and .password to get values
    return keyring.get_credential(credName, None)