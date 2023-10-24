import re

data_list = ['ABC', ' BANK', 'Fue williag,', 'NO DEBIT/CREDIT & BLOCK STATUS MARKING FORM',
             'Date:    2023/02/32', 'Branch:',
             '001-MURREE ROAD RWP BRANCH',
             'Account No:','0932435356332206 Title of Account:','muneeb tabassum',
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
    # print(item)
    match_date = re.search(date_pattern, item)
    match_test = re.search(test_pattern, item)
    match_branch = re.search(branch_pattern, item)
    match_account_no = re.search(account_no_pattern, item)
    match_account_title = re.search(account_title_pattern, item)

    if match_account_title:
        # print(item)
        split_item = item.split(':')
        # print(split_item)
        if split_item[-1] == '':
            print("index based")
            # print(True)
            idx = data_list.index(match_account_title.group(0))
            # print(idx+1)
            # print(data_list[idx+1])
            if data_list[idx+1].startswith('Rational'):
                data_dict['account_title'] = None
            else:
                data_dict['account_title'] = data_list[idx+1].strip()
        else:
            print("colon based")
            # print(split_item[-1])
            data_dict['account_title'] = split_item[-1].strip()

    if match_date:
        # print(match_date.group(0))
        data_dict['date'] = match_date.group(0)
    if match_test:
        # print(match_test.group(0))
        data_dict['test'] = match_test.group(0)
    if match_branch:
        # print(match_branch.group(0))
        data_dict['branch'] = match_branch.group(0)
    if match_account_no:
        # print(match_account_no.group(0))
        data_dict['account_no'] = match_account_no.group(0)

for key, value in data_dict.items():
    if value == '':
        data_dict[key] = None


print(data_dict)




