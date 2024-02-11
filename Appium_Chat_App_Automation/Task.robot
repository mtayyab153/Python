*** Settings ***
Library  AppiumLibrary

*** Variables ***

*** Keywords ***
Open Chat21 Applicaiton
    Open Application
    ...  http://localhost:4723
    ...  platformName=Android
    ...  deviceName=emulator-5554
    ...  appPackage=chat21.android.demo
    ...  appActivity=chat21.android.demo.SplashActivity
    ...  automationName=Uiautomator2

    ${pop_up_status}=  Run Keyword And Return Status    Page Should Contain Element    //android.widget.Button[@text='Continue']
    Run Keyword If    '${pop_up_status}'=='True'    ByePass Android 10 Popups

ByePass Android 10 Popups
    Wait Until Page Contains Element    //android.widget.Button[@text='Continue']
    Click Element    //android.widget.Button[@text='Continue']
    Sleep    3s
    Wait Until Page Contains Element    //android.widget.Button[@text='OK']
    Click Element    //android.widget.Button[@text='OK']

    Log    Hi
    #    Click Element    id=com.android.permissioncontroller:id/continue_button
Login to Chat21 App
    [Arguments]  ${user_email}  ${user_password}
    Wait Until Page Contains Element    id=chat21.android.demo:id/email
    Input Text    id=chat21.android.demo:id/email    ${user_email}
    Input Password    id=chat21.android.demo:id/password    ${user_password}
    Click Element    id=chat21.android.demo:id/login
    Wait Until Page Contains Element    //android.widget.Button[@text='SELECT A CONTACT']  20s

Get User Details
    Wait Until Page Contains Element    //android.widget.TextView[@text='PROFILE']
    Click Element    //android.widget.TextView[@text='PROFILE']
    Wait Until Page Contains Element    id=chat21.android.demo:id/fullname
    ${user_name}=  Get Text    id=chat21.android.demo:id/fullname
    ${user_email}=  Get Text    id=chat21.android.demo:id/email

Logout Chat21 App
#    Wait Until Page Contains Element    //android.widget.TextView[@text='PROFILE']
#    Click Element    //android.widget.TextView[@text='PROFILE']
    Wait Until Page Contains Element    id=chat21.android.demo:id/logout
    Click Element    id=chat21.android.demo:id/logout
*** Tasks ***
Android App Automation
    Open Chat21 Applicaiton

    #    First user
    Login to Chat21 App  testing1@gmail.com  testing1
    Get User Details
    Logout Chat21 App

    #    Second user
    Login to Chat21 App  testing3@gmail.com  testing3
    Get User Details
    Logout Chat21 App