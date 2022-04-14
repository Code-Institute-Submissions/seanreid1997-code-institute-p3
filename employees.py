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
    user_input_view = input('Would you like to view our list of employees?\n')
    if user_input_view == 'yes':
        print('Retrieving list of employees. Please wait...\n')
        view_employees()
    else:
        pass

    user_input_add = input('Would you like to add an employee?\n')
    if user_input_add == 'yes':
        add_employee()
    else:
        pass

    user_input_remove = input('Would you like to remove an employee?\n')
    if user_input_remove == 'yes':
        remove_employee()
    else:
        print('Thank you for using our services.\n')


def add_employee():
    """
    Function that enables user to add an employee
    and their details to the compamy spreadsheet.
    """
    add_staff = input('Please enter employee details(name,job,income):\n')
    staff_data = add_staff.split(',')
    print("Updating Employee data. Please wait...\n")
    worksheet_to_update = SHEET.worksheet('Employees')
    worksheet_to_update.append_row(staff_data)
    print("Employee data successfully added.\n")


def remove_employee():
    """
    Function that allows user to remove an employee
    and their details from the company spreadsheet.
    """
    remove_staff = input('Please enter employee details(name,job,income):\n')
    print("Removing Employee data. Please wait...\n")
    worksheet_to_update = SHEET.worksheet('Employees')
    worksheet_to_update.delete_rows(remove_staff)
    print("Employee data successfully added.\n")


def view_employees():
    """
    Function that allows user to view all current employees.
    """
    employee = SHEET.worksheet('Employees').get_all_values()
    staff = []
    for staff in employee:
        print(staff)
