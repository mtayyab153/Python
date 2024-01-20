import paramiko


class AutomationScript:
    def create_connection_and_execute_commands(self):
        hostname = 'x.x.x.x'
        port = 22
        username = 'testing'
        password = 'testing'

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)

        # command = "pwd"
        command = "cd .android && adb -s 75d2e2fe shell && cd data/ExternalModules/logs && ls"
        stdin, stdout, stderr = ssh.exec_command(command)

        output = stdout.read().decode()
        print(output)

        return output

        ssh.close()
