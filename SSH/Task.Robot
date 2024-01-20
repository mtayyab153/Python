*** Settings ***
Library  AutomationScript.py
Library    String

*** Variables ***


*** Keywords ***
Make connection
    ${res}=  create_connection_and_execute_commands
    Log    ${res}


*** Test Cases ***
Automating a Use Case
    Make connection