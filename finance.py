import gspread
from google.oauth2.service_account import Credentials
from run import main
from run import menu

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
    return_menu = input('\n')
    return_home = input('\n')

    if finance_user_input == '1':
        data = financial_data.get_all_values()
        print(data)
        print('1.Return to menu')
        print('2.Return to home')

        if return_menu == '1':
            menu()

        if return_home == '2':
            main()

    if finance_user_input == '2':
        last_row_data = [financial_data.get_all_values()][-1]
        print(last_row_data)

        if return_menu == '1':
            menu()

        if return_home == '2':
            main()
