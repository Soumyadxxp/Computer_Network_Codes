def ipClassFinder(ipAdress):
    ipPrefix=int(ipAdress.split(".")[0])
    if ipPrefix in range(0,127):
        print("Class A IP Adress")
    elif ipPrefix in range(128,191):
        print("Class B IP Adress")
    elif ipPrefix in range(192,223):
        print("Class C IP Adress")
    elif ipPrefix in range(224,239):
        print("Class D IP Adress")
    elif ipPrefix in range(240,255):
        print("Class E IP Adress")
    else:
        print("Invalid IP Adress")

ip=input("Enter an IP Adress: ")
ipClassFinder(ip)