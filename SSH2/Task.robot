*** Settings ***
Library  SSHLibrary


*** Variables ***
${HOST_IP}   x.x.x.x
${HOST_USERNAME}  testing
${HOST_PASSWORD}  testing

*** Keywords ***
Create connection
    Open Connection  ${HOST_IP}
    Login  ${HOST_USERNAME}  ${HOST_PASSWORD}

Execute a command
#    ${command}  Set Variable  ls && cd testing && pwd && ls -ltr
    ${command}  Set Variable  cd .android && adb -s 55 shell && cd data/ExternalModules/logs && ls
    ${output}=  Execute Command  ${command}
    Log    ${output}


*** Test Cases ***
Automating a Use Case
    Create connection
    Execute a command