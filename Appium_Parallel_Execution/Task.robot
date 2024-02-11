*** Settings ***
Library  AppiumLibrary

*** Variables ***

*** Keywords ***
Open Chorme Applicaiton
    Open Application
    ...  http://localhost:4723
#    ...  http://localhost:4725
    ...  platformName=Android
    ...  appPackage=com.android.chrome
    ...  appActivity=org.chromium.chrome.browser.document.ChromeLauncherActivity
    ...  automationName=Uiautomator2

*** Tasks ***
Android App Automation
    Open Chorme Applicaiton
