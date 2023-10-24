import re

data_list = ['ABC', ' BANK', 'Fue williag,', 'NO DEBIT/CREDIT & BLOCK STATUS MARKING FORM',
       'Date:', '2023/09/13', 'Branch:', '001-MURREE ROAD RWP BRANCH',
       'Account No:0923243535633220', 'Title of Account:Muneeb Tabassum',
       'Rationale for Marking Block Status: Loan', 'Amount to be blocked: 1,000.26', 'Applicable Date of NDS:',
       'Block Removal Date:', '(if marked for specific term)', 'Hold Code:', 'OMD', 'Lond', 'Requested By',
       'Approved By', 'FOR CPU USE ONLY', 'Processed By:', 'Authorized By:', 'Signature', 'Signature']

data_dict = {}

# Regular expressions to match the title of account
date_pattern = r'\b(\d{2}[/|-]\d{2}[/|-]\d{4}|\d{4}[/|-]\d{2}[/|-]\d{2})\b'
test_pattern = 'FOR CPU USE ONLY'
branch_pattern = r'\d{3,4}-[A-Z\s]+'
account_no_pattern = r'\d{9,16}'
account_title_pattern = r'Title of Account:(.*)'
account_title_pattern_2 = r'Title of Account:,\s?(.*)'

# Flag to check if the title is part of the same item
title_part_of_item = False

for item in data_list:
  match_date = re.search(date_pattern, item)
  match_test = re.search(test_pattern, item)
  match_branch = re.search(branch_pattern, item)
  match_account_no = re.search(account_no_pattern, item)

  # Use a re.findall() function to match the account title in both scenarios
  match_account_title = re.findall(account_title_pattern + '|' + account_title_pattern_2, item)

  # If the match_account_title list is not empty, use the first element of the list as the account title
  if match_account_title:
    account_title = match_account_title[0].strip()
    if account_title:
      data_dict['account_title'] = account_title
      title_part_of_item = True

  # Check if the title is in the next item
  elif title_part_of_item:
    account_title = item.strip()
    if account_title:
      data_dict['account_title'] = account_title
      title_part_of_item = False

print(data_dict)