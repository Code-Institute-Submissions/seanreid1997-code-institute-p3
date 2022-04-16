import os
import time
import gspread
from google.oauth2.service_account import Credentials
from employees import options
from employees import manage_spreadsheet
from finance import get_finance_data

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
    print('\n1.Yes')
    print('2.No')
    user_registered = input('Do you have an account?\n')
    update_register = SHEET.worksheet('Login')
    time.sleep(0.3)
    if user_registered == '1':
        clear_console()
        welcome_message()
        login()
    elif user_registered == '2':
        user = input('\nPlease enter your username:\n')
        time.sleep(0.19)
        user_password = input('Please enter your password:\n')
        new_user = user, user_password
        print('\nRegistering your details...\n')
        time.sleep(0.2)
        update_register.append_row(new_user)
        print('\nUser successfully added')
        time.sleep(0.2)
    else:
        print('Invalid')


def login():
    """
    Function that collects user login credentials
    and compares them to credentials on spreadsheet
    """
    time.sleep(0.2)
    authorise = SHEET.worksheet('Login')
    verify_name = authorise.col_values(1)
    verify_password = authorise.col_values(2)

    while True:
        username = input('\nUsername:\n')
        if username in verify_name:
            print('\nUsername is correct\n')
        else:
            print('\nYour username is incorrect. Please try again!\n')
            clear_console()
            welcome_message()
            login()

        password = input('Password:\n')
        if password in verify_password:
            print('\nPassword is correct')
            print('Please wait...')
            time.sleep(3)
            print('You successfully logged in!\n')
            return True
        else:
            print('\nYour password is incorrect. Please try again!\n')
            clear_console()
            main()


def clear_console():
    """
    Clears the console
    """
    time.sleep(1)
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def menu():
    """
    Function that provides a menu for users
    to procede.
    """
    clear_console()
    time.sleep(0.3)
    print('Menu')
    print('1.Manage employee worksheet')
    print('2.Manage finance worksheet')
    print('3.Manage spreadsheet')
    user_choice = input('\n')

    if user_choice == '1':
        clear_console()
        options()
        exit_program()

    elif user_choice == '2':
        clear_console()
        get_finance_data()

        print('\n1.Return to menu')
        print('2.Return to home')
        user_return = input('\n')

        if user_return == '1':
            menu()

        if user_return == '2':
            exit_program()

    elif user_choice == '3':
        clear_console()
        manage_spreadsheet()
        exit_program()


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
    exit_program()


main()
