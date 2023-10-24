# Extract and validate the following:
# Date
# Branch Code
# Account no
# Account title
# reason
# CNIC
# contact no

import re
from datetime import datetime

data_list = ['MICHOFINANCE BANK', 'HBL', 'Time: 18:27:19', 'Date: ' ,'25/08/2023', '| he Branch Manager,', 'I IBL Microfinance Bank Ltd.',
'MIAN CHANNU BRANCH', 'Branch Code: 184', 'Request for Activation of Dormant Account No. 1841041387543017',
'/We, Mr./Ms./Mrs/Messer SHAZIA has/ have been maintaining the above account with you.',
'The said bank account has not been operated by me/us for a long time due to reason OUT OF CITY   I / We understand',
'that due to safeguard the interest of customers, Bank has classified the said account as "dormant".',
'I/ We now agree to operate the said bank account regularly and request you to re-classify the account as "active".',
'| am / we are also agreed to pay all the pending / recoverable charges in my account.', 'Yours truly,',
'SECURITY BANK COMPANY', 'and', 'Rundi', 'ANOE', 'Customer Signature / Thumb Impression', 'Contact No: 03176123506',
'CNIC # : 3610404461568', 'RECEIVED', 'SEP', 'BANK', 'FOR BRANCH USE',
'Recent Income Proof Obtained (In case of change in occupation/business or if not already available',
'NADRA Verisys Obtained (in case of renewal)', '25', 'CNIC Expiry Updated (In case of renewal)',
'SEP', 'Custom', 'CIF/KYC Updation Request obtained (If there is change in CiF information/ transactions turnover)',
 'We confirm the fulfillment of all formalities for activation of dormant account as described in operations manual and',
'circulars issued by the bank from time to time.', 'Dist', 'Branch Operation In-Charge', 'Branch Manager', "For CPU'USE", 'Processed By:', 'Authorized By:', 'Signature', 'Signature']

def validate_date(input_date):
    try:
        dateObject = datetime.strptime(input_date, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def get_data_as_per_requirements(data_list):
    date_pattern = r'\b(\d{2}/\d{2}/\d{4})\b'
    branch_code_pattern = r'\b(\d{3})\b'
    account_no_pattern = r'\b(\d{16})\b'
    account_title_pattern = r'Messer\s(.*?)\shas/'
    cnic_pattern = r'\b(\d{13})\b'
    contact_no_pattern = r'\b(\d{11})\b'
    dormancy_reason_pattern = r'reason\s(.*?)\sI\s/'


    for item in data_list:
        match_date = re.search(date_pattern, item)
        match_branch_code = re.search(branch_code_pattern, item)
        match_account_no = re.search(account_no_pattern, item)
        match_account_title = re.search(account_title_pattern, item)
        match_cnic = re.search(cnic_pattern, item)
        match_contact_no = re.search(contact_no_pattern, item)
        match_dormancy_reason = re.search(dormancy_reason_pattern, item)

        if match_date:
            date = match_date.group(0)
            if validate_date(date):
                data_dict['date'] = date
            else:
                data_dict['date'] = 'Invalid Date.'

        if match_branch_code:
            branch_code = match_branch_code.group(1)
            data_dict['branch_code'] = branch_code


        if match_account_no:
            account_number = match_account_no.group(0)
            try:
                if branch_code == account_number[:3]:
                    data_dict['account_number'] = account_number
                else:
                    data_dict['account_number'] = "Branch Code doesn't matches."
            except:
                data_dict['account_number'] = account_number

        if match_account_title:
            data_dict['account_title'] = match_account_title.group(1).strip().upper()

        if match_dormancy_reason:
            data_dict['dormancy_reason'] = match_dormancy_reason.group(1).strip().upper()

        if match_cnic:
            cnic = match_cnic.group(1)
            data_dict['cnic'] = cnic

        if match_contact_no:
            contact = match_contact_no.group(1)
            data_dict['contact_no'] = contact


data_dict = {
    'date': 'Invalid Date. Date must be in dd/mm/yyyy format.',
    'branch_code': 'Invalid Branch Code. Branch Code must be 3 digits.',
    'account_number': 'Invalid Account Number. Account Number must be 16 digits.',
    'account_title': 'Invalid Title',
    'dormancy_reason': 'Invalid Dormancy Reason',
    'contact_no': 'Invalid Contact No. Contact No must be 11 digits.',
    'cnic': 'Invalid CNIC. CNIC must be 13 digits.'
}

get_data_as_per_requirements(data_list)

print(data_dict)