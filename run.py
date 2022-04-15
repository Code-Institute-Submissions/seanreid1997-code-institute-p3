from employees import options
from employees import create_worksheet


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


def login():
    """
    Function that collects user login credentials
    and compares them to credentials on spreadsheet
    """
    input('\nEnter Username:\n')
    input('Enter Password\n')


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
    create_worksheet()
    

main()
