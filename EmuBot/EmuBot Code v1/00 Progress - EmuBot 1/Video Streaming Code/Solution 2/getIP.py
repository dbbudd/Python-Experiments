import socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("192.168.100.1", 80))
    return s.getsockname()[0]

print(get_ip_address())