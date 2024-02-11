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

Other Keywords in Appium Library
    ${activity_name}=  Get Activity
    ${appium_s_id}=  Get Appium SessionId
    ${appium_default_timeout}=  Get Appium Timeout
    ${device_name}=  Get Capability    deviceName
    ${contexts}=  Get Contexts
    ${curr_context}=  Get Current Context
    ${elem_dims}=  Get Element Rect    id=com.google.android.calculator:id/digit_9
    ${elem_size}=  Get Element Size    id=com.google.android.calculator:id/digit_9
    ${net_stats}=  Get Network Connection Status
    ${curr_page_src}=  Get Source
    ${res}=  Get Text    id=com.google.android.calculator:id/result_preview
    ${device_height}=  Get Window Height
    ${device_width}=  Get Window Width
#    ${window_title}=  Get Window Title
#    ${window_url}=  Get Window Url
#    Go To Url    https://www.google.com
#    Go Back
    Hide Keyboard
    ${keyboard_status}=  Is Keyboard Shown
    Landscape
    Portrait
#    Open Notifications
#    Sleep    3s
#    Swipe    500    100    100    0
#    Swipe By Percent	90	50	10	50
#    Shake
#    Start Screen Recording  timeLimit=10s
#    Stop Screen Recording  filename=output


*** Tasks ***
Automate an Android Calculator App
    Open Calculator App
    Add two numbers
    Other Keywords in Appium Library
#    Close Application
#    Quit Application