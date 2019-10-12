"""
SSH 连接交互
"""
import os
import paramiko

hostname = "192.168.10.104"
port = 22
username = "root"
password = "qazwsx"

def simple_example():
    ssh = paramiko.SSHClient()
    know_host = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(know_host)
    ssh.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password
    )
    cmd = 'ls'
    stdin,stdout,stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    ssh.close()



def shell_invoke():
    ssh = paramiko.SSHClient()
    know_host = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(know_host)
    ssh.connect(
        hostname=hostname,
        port=port,
        username=username,
        password=password
    )
    shell = ssh.invoke_shell()
    shell.settimeout(1)

    command = input(">>>" + "\n")
    shell.send(command)
    while True:
        try:
            recv = shell.recv(512).decode()
            if recv:
                print(recv, end='')
            else:
                continue
        except:
            command = input("") + "\n"
            shell.send(command)


def file_upload_download():
    trans = paramiko.Transport(
        sock=(hostname, port)
    )
    trans.connect(
        username=username,
        password=password
    )
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put("ssh_connect.py", "/root/stark/ssh_connect.py")

    if not os.path.exists(r'cache'):
        os.mkdir(r'cache')
    sftp.get("/root/stark/ssh_connect.py","cache/ssh_connect.py")
    sftp.close()


# simple_example()
shell_invoke()
# file_upload_download()

