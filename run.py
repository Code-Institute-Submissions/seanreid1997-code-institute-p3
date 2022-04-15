import time
import gspread
from google.oauth2.service_account import Credentials
from employees import options

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Tech Company ltd")
BORDER = '_' * 50
WELCOME = '\nWelcome to The Tech Company data service\n'


def welcome_message():
    """
    Prints out a welcome message at the begining
    of the program
    """
    print(BORDER)
    print(BORDER)
    print(WELCOME.center(20).upper())
    print(BORDER)
    print(BORDER)


def login():
    """
    Function that collects user login credentials
    and compares them to credentials on spreadsheet
    """
    authorise = SHEET.worksheet('Login')
    verify_name = authorise.col_values(1)
    verify_password = authorise.col_values(2)

    while True:
        username = input('\nUsername:\n')
        if username in verify_name:
            print('\nUsername is correct\n')
        else:
            print('Your username is incorrect. Please try again!')

        password = input('Password:\n')
        if password in verify_password:
            print('\nPassword is correct')
            print('Please wait...')
            time.sleep(3)
            print('Successfully logged in!\n')
            time.sleep(2)
            print('Choose from the following:\n')
            return True
        else:
            print('Your password is incorrect. Please try again!')


def menu():
    """
    Function that provides a menu for users
    to procede.
    """


def main():
    """
    Runs all functions in the program.
    """
    welcome_message()
    login()
    options()
  

main()
