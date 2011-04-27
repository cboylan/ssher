import argparse
import paramiko

class Client(object):
    def __init__(self, args):
        self._client = paramiko.SSHClient()
        self._uname = args["uname"]
        self._p1 = args["passwd1"]
        self._p2 = args["passwd2"]
        self._server = args["server"]

    def connect(self):
        self._client.load_system_host_keys()
        self._client.connect(self._server, username=self._uname, password=self._p1)

    def run(self, cmd):
        stdin, stdout, stderr = self._client.exec_command(cmd)
        return stdout

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Python ssh client.")
    parser.add_argument("-u", "--uname", help = "username to connect with")
    parser.add_argument("-p1", "--passwd1", help = "primary user passwd")
    parser.add_argument("-p2", "--passwd2", help = "secondary user passwd")
    parser.add_argument("server", help = "server to connect to")
    args = parser.parse_args()

    client = Client(vars(args))
    client.connect()
    output = client.run("ls -l")
    print(output)
