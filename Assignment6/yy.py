import re

data_list = ['ABC', ' BANK', 'Fue williag,', 'NO DEBIT/CREDIT & BLOCK STATUS MARKING FORM',
             'Date:    2023/02/32', 'Branch:',
             '001-MURREE ROAD RWP BRANCH',
             'Account No:0932435356332206755767 Title of Account:','muneeb tabassum',
             'Rationale for Marking Block Status: Loan', 'Amount to be blocked: 1,000.26', 'Applicable Date of NDS:',
             'Block Removal Date:', '(if marked for specific term)', 'Hold Code:', 'OMD', 'Lond', 'Requested By',
             'Approved By', 'FOR CPU USE ONLY', 'Processed By:', 'Authorized By:', 'Signature', 'Signature']

date_pattern = r'\b(\d{2}[/|-]\d{2}[/|-]\d{4}|\d{4}[/|-]\d{2}[/|-]\d{2})\b'
test_pattern = 'FOR CPU USE ONLY'
branch_pattern = r'\d{3,4}-[A-Z\s]+'
account_no_pattern = r'\d{9,16}'
account_title_pattern = r'.*Title of Account.*'

data_dict = {
    'date': None,
    'test': None,
    'branch': None,
    'account_no': None,
    'account_title': None
}

for item in data_list:
    match_date = re.search(date_pattern, item)
    match_test = re.search(test_pattern, item)
    match_branch = re.search(branch_pattern, item)
    match_account_no = re.search(account_no_pattern, item)
    match_account_title = re.search(account_title_pattern, item)

    if match_account_title:
        split_item = item.split(':')
        if split_item[-1] == '':
            idx = data_list.index(match_account_title.group(0))
            if data_list[idx+1].startswith('Rational'):
                data_dict['account_title'] = None
            else:
                data_dict['account_title'] = data_list[idx+1].strip()
        else:
            data_dict['account_title'] = split_item[-1].strip()

    if match_date:
        data_dict['date'] = match_date.group(0)
    if match_test:
        data_dict['test'] = match_test.group(0)
    if match_branch:
        data_dict['branch'] = match_branch.group(0)
    if match_account_no:
        account_no = match_account_no.group(0)
        if len(account_no) > 16:
            data_dict['account_no'] = None
        else:
            data_dict['account_no'] = account_no

print(data_dict)
