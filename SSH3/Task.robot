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
    Write    cd android
    Write    cd 75
    Write    cd data
    Write    cd ExternalModules
    Write    cd logs
    Write    ls
    ${output}=  Read
    Log    ${output}


*** Test Cases ***
Automating a Use Case
    Create connection
    Execute a command