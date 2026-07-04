import socket
def ipClassFinder(ipAdress):
    ipPrefix=int(ipAdress.split(".")[0])
    if ipPrefix>=0 and ipPrefix<=127:
        print("Class A IP Adress")
    elif ipPrefix>=128 and ipPrefix<=191:
        print("Class B IP Adress")
    elif ipPrefix>=192 and ipPrefix<=223:
        print("Class C IP Adress")
    elif ipPrefix>=224 and ipPrefix<=239:
        print("Class D IP Adress")
    elif ipPrefix>=240 and ipPrefix<=255:
        print("Class E IP Adress")
    else:
        print("Invalid IP Adress")


def get_local_ip():
    """Retrieves the local IP address of the machine."""
    try:
        # Get the hostname
        hostname = socket.gethostname()
        # Get the IP address by passing the hostname
        ip_address = socket.gethostbyname(hostname)
        ipClassFinder(ip_address)
        print(ip_address)
    except socket.error as e:
        return f"Error getting local IP address: {e}"

get_local_ip()