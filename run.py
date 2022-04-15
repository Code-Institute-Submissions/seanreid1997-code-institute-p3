import os
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
    print(WELCOME.upper())
    print(BORDER)
    print(BORDER)


def register():
    """
    Function to allow user to register their login
    credentials
    """
    user_registered = input('Do you have an account?\n')
    update_register = SHEET.worksheet('Login')
    time.sleep(1)
    if user_registered == 'yes':
        login()
    else:
        user = input('Please enter your username:\n').capitalize()
        user_password = input('Please enter your password:\n')
        new_user = user, user_password
        update_register.append_row(new_user)
        print('User successfully added')


def login():
    """
    Function that collects user login credentials
    and compares them to credentials on spreadsheet
    """
    time.sleep(0.4)
    authorise = SHEET.worksheet('Login')
    verify_name = authorise.col_values(1)
    verify_password = authorise.col_values(2)

    while True:
        username = input('\nUsername:\n').capitalize()
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
            return True
        else:
            print('Your password is incorrect. Please try again!')


def clear_console():
    """
    Clears the console
    """
    time.sleep(2)
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def menu():
    """
    Function that provides a menu for users
    to procede.
    """
    time.sleep(1)
    print('Choose from the following:\n')
    user_choice = print('1.Manage employee worksheet')
    user_choice2 = print('2.Manage finance worksheet')
    user_choice3 = print('3.Manage spreadsheet')

    if 
    input('\n')


def exit_program():
    """
    Function that returns program to the begining
    once user has completed use.
    """
    clear_console()
    time.sleep(1)
    main()


def main():
    """
    Runs all functions in the program.
    """
    welcome_message()
    register()
    clear_console()
    menu()
    options()
    exit_program()


main()
