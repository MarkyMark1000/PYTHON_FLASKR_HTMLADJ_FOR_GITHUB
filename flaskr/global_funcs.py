import socket


def get_ip(testException=False):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        if testException:
            raise Exception("Test Exception")
    except Exception as Ex:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
