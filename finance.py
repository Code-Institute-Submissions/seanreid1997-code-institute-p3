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
financial_data = SHEET.worksheet('Finance')


def get_finance_data():
    """
    Function that retrieves financial data from
    finance worksheet
    """
    print('1.View all financial data')
    print('2.View last entry')
    finance_user_input = input('\n')

    if finance_user_input == '1':
        full_statement = SHEET.worksheet('Finance').get_all_values()
        for data in full_statement:
            print(data)

def monthly_profit():
    """
    Function that gets values from the 2 columns
    in 'Finance' worksheet and subtracts
    the latter from the first. (column 1 - column 2)
    """