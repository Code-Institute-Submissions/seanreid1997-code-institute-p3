import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Tech Company ltd")

def options():
    """
    Provides options to the user 
    and then calls the funtion relevant to the answer given by user.
    """


def add_user():
    """
    Function that enables user to add an employee
    and their details to the compamy spreadsheet.
    """


def remove_user():
    """
    Function that allows user to remove an employee
    and their details from the company spreadsheet
    """


def employee_details():
    """
    Get the name and employment details of all people currently employed by the company
    """
    employee = SHEET.worksheet('Employees')
    for x in employee.get_all_values():
        if x == "Alim":
            return x
    print(employee.row_values(4))  
 

def main():
    """
    Runs all functions in the program
    """
    


