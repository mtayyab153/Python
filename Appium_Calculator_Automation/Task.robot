*** Settings ***
Library  AppiumLibrary

*** Variables ***


*** Keywords ***
Open Calculator App
    Open Application
    ...  http://localhost:4723
    ...  platformName=Android
    ...  deviceName=emulator-5554
    ...  appPackage=com.google.android.calculator
    ...  appActivity=com.android.calculator2.Calculator
    ...  automationName=Uiautomator2

Add two numbers
    Clear Text    id=com.google.android.calculator:id/formula
    Wait Until Page Contains Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/op_add
    Click Element    id=com.google.android.calculator:id/digit_9
    ${res}=  Get Text    id=com.google.android.calculator:id/result_preview
    Log    ${res}

Subtract two numbers
    Clear Text    id=com.google.android.calculator:id/formula
    Wait Until Page Contains Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/op_sub
    Click Element    id=com.google.android.calculator:id/digit_9
    ${res}=  Get Text    id=com.google.android.calculator:id/result_preview
    Log    ${res}

Multiply two numbers
    Clear Text    id=com.google.android.calculator:id/formula
    Wait Until Page Contains Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/op_mul
    Click Element    id=com.google.android.calculator:id/digit_9
    ${res}=  Get Text    id=com.google.android.calculator:id/result_preview
    Log    ${res}

Divide two numbers
    Clear Text    id=com.google.android.calculator:id/formula
    Wait Until Page Contains Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/op_div
    Click Element    id=com.google.android.calculator:id/digit_9
    ${res}=  Get Text    id=com.google.android.calculator:id/result_preview
    Log    ${res}


*** Tasks ***
Automate an Android Calculator App
    Open Calculator App
    Add two numbers
#    Subtract two numbers
#    Multiply two numbers
#    Divide two numbers
    Close Application