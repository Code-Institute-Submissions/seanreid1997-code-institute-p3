import time
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
    print('\nPlease select from the following\n')
    print('1.Yes')
    print('2.No')
    user_input_view = input('Would you like to view our list of employees?\n')
    if user_input_view == '1':
        print('Retrieving list of employees. Please wait...\n')
        view_employees()
        time.sleep(0.3)
    else:
        pass
    
    print('\n1.Yes')
    print('2.No')
    user_input_add = input('\nWould you like to add an employee?\n')
    if user_input_add == '1':
        add_employee()
        time.sleep(0.3)
    else:
        pass

    print('\n1.Yes')
    print('2.No')
    user_input_remove = input('\nWould you like to remove an employee?\n')
    if user_input_remove == '1':
        remove_employee()
        time.sleep(0.3)
    else:
        print('\nThank you for using our services.\n')
        time.sleep(0.5)


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
    remove_staff = input('Please enter employee details(Name, Job title, \
                                                        Income):\n')
    print("Removing Employee data. Please wait...\n")
    worksheet_to_update = SHEET.worksheet('Employees')
    worksheet_to_update.delete_rows(remove_staff)
    print("Employee data successfully added.\n")


def view_employees():
    """
    Function that allows user to view all current employees.
    """
    SHEET.worksheet('Employees')
    employee = SHEET.worksheet('Employees').get_all_values()
    staff = []
    for staff in employee:
        print(staff)


def create_worksheet():
    """
    Functions that create a new worksheet
    """
    wsheet_name = input('Please enter the worksheet name:\n')
    wsheet_col = input('Please enter the number of columns:\n')
    wsheet_rows = input('Please enter the number of rows:\n')
    print('\nCreating worksheet. Please wait...\n')
    SHEET.add_worksheet(wsheet_name, wsheet_rows, wsheet_col)
    print('Worksheet successfully created\n')


def delete_worksheet():
    """
    Function that allows user to
    deletes selected worksheet
    """
    input('Please enter the worksheet name:\n')
    print('\nDeleting worksheet. Please wait...\n')
    SHEET.del_worksheet('bb')
    print('worksheet has been successfully deleted.')


def manage_spreadsheet():
    """
    Function that allows user to manage all
    worksheets in spreadsheets.
    """
    user_input_create = input('\nWould you like to create a worksheet?\n')
    if user_input_create == 'yes':
        create_worksheet()
        time.sleep(0.3)
    else:
        pass

    user_input_delete = input('\nWould you like to delete a worksheet?\n')
    if user_input_delete == 'yes':
        delete_worksheet()
        time.sleep(0.3)
    
    print('\nThank you for using our services.\n')