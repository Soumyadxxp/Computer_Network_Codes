class IP:
    def __init__(self, address):
        self.address = address
        self.network_type = self._typeOfANetwork()
        self.ip_range = self._ipRangeFind()
        self.default_mask = self._getDefaultMask()
        self.subnet_mask = self._subnetMaskFind()
        self.broadcast_address = self._broadcastAddressFind()
        self.prefixLength=self._getPrefixLength()
        self.hosts=self._hostAvailable()
    
    def _getPrefixLength(self):
        ipPrefix = int(self.address.split(".")[0])
        if ipPrefix in range(0, 128):
            return 8
        elif ipPrefix in range(128, 192):
            return 16
        elif ipPrefix in range(192, 224):
            return 24
        else:
            return None

    def _typeOfANetwork(self):
        try:
            ipPrefix = int(self.address.split(".")[0])
            if ipPrefix in range(0, 128):
                return "Class A"
            elif ipPrefix in range(128, 192):
                return "Class B"
            elif ipPrefix in range(192, 224):
                return "Class C"
            elif ipPrefix in range(224, 240):
                return "Class D"
            elif ipPrefix in range(240, 256):
                return "Class E"
            else:
                print("Invalid IP Adress")
        except (ValueError, AttributeError):
            return "Invalid IP Address"

    def _ipRangeFind(self):
        if self.network_type == "Class A":
            return ("0.0.0.0", "127.255.255.255")
        elif self.network_type == "Class B":
            return ("128.0.0.0", "191.255.255.255")
        elif self.network_type == "Class C":
            return ("192.0.0.0", "223.255.255.255")
        elif self.network_type == "Class D":
            return ("224.0.0.0", "239.255.255.255")
        elif self.network_type == "Class E":
            return ("240.0.0.0", "254.255.255.255")
        else:
            return ("", "")

    def _getDefaultMask(self):
        ipPrefix = int(self.address.split(".")[0])
        if ipPrefix in range(0, 128):
            return "255.0.0.0"
        elif ipPrefix in range(128, 192):
            return "255.255.0.0"
        elif ipPrefix in range(192, 224):
            return "255.255.255.0"
        elif ipPrefix in range(224, 240):
            return "255.255.255.255"
        else:
            return "N/A"

    def _subnetMaskFind(self):
        octets = list(map(int, self.address.split(".")))
        subnet_octets = list(map(int, self.default_mask.split(".")))

        octets_bin = [f"{o:08b}" for o in octets]
        subnet_octets_bin = [f"{s:08b}" for s in subnet_octets]

        masks = []
        for octet, subnet_octet in zip(octets_bin, subnet_octets_bin):
            mask_octet = ""
            for octet_bit, subnet_bit in zip(octet, subnet_octet):
                if octet_bit == "1" and subnet_bit == "1":
                    mask_octet += "1"
                else:
                    mask_octet += "0"
            masks.append(mask_octet)

        masks_int = [int(mask, 2) for mask in masks]
        return ".".join([str(mask) for mask in masks_int])

    def _broadcastAddressFind(self):
        octets = list(map(int, self.address.split(".")))
        subnet_octets = list(map(int, self.default_mask.split(".")))
        network_bits = [oc & sc for oc, sc in zip(octets, subnet_octets)]
        wildcard_bits = [255 - sc for sc in subnet_octets]
        broadcast_bits = [nw | wc for nw, wc in zip(network_bits, wildcard_bits)]
        
        return ".".join(map(str, broadcast_bits))
    
    def _hostAvailable(self):
        if self.prefixLength==None:
            return None
        hosts=2**(32-int(self.prefixLength))-2
        return hosts

    def displayIPInfo(self):
        print("=" * 40)
        print(f"IP Address: {self.address}")
        print(f"Class IP: {self.network_type}")
        print(f"IP Range: {self.ip_range[0]} - {self.ip_range[1]}")
        print(f"Address Mask: {self.subnet_mask}")
        print(f"Broadcast Addess: {self.broadcast_address}")
        print(f"Available Hosts  : {'N/A' if self.hosts is None else self.hosts}")

def main():
    ipList = [IP("192.168.100.14"), IP("172.16.100.55"), IP("10.56.42.5")]

    for ip in ipList:
        ip.displayIPInfo()


if __name__ == "__main__":
    main()
    print("=" * 40)
