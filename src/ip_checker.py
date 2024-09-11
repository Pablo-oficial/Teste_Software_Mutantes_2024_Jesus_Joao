import re

class ip_check:
    """
    Check the validity and class of an IP address.

    :validate_it: Verify the IP address.
    :find_class: Find the class of the IP address.
    :format_ip: Format the IP address to standard notation.
    :ip_to_int: Convert the IP address to an integer.
    :is_reserved_ip: Check if the IP address is a reserved IP address.
    """
     
    def __init__(self, IP):
        self.IP = IP
    
    def validate_it(self):
        """
        Check the validity of an IP address.
        :return: The type of IP address. Returns 'Invalid IP' for invalid IP address.
        """
        # Regex expression for validating IPv4
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        
        # Regex expression for validating IPv6
        regex1 = "((([0-9a-fA-F]){1,4})\\:){7}([0-9a-fA-F]){1,4}"
        
        # Compiling the regex expressions
        p = re.compile(regex)
        p1 = re.compile(regex1)

        # Checking if it is a valid IPv4 address
        if (re.search(p, self.IP)):
            return "Valid IPv4"
        
        # Checking if it is a valid IPv6 address
        elif (re.search(p1, self.IP)):
            return "Valid IPv6"
        
        return "Invalid IP"
   

    def find_class(self):
        """
        Find out the class of an IP address.
        :return: The class of the IP address.
        """
        if self.validate_it() != "Valid IPv4":
            return "N/A"  # Not applicable for non-IPv4 addresses

        ip = self.IP.split(".")
        ip = [int(i) for i in ip]
        
        # If ip[0] >= 0 and ip[0] <= 127 then the IP address is in class A
        if ip[0] >= 0 and ip[0] <= 127:
            return "A"
        
        # If ip[0] >= 128 and ip[0] <= 191 then the IP address is in class B
        elif ip[0] >= 128 and ip[0] <= 191:
            return "B"
        
        # If ip[0] >= 192 and ip[0] <= 223 then the IP address is in class C
        elif ip[0] >= 192 and ip[0] <= 223:
            return "C"
        
        # If ip[0] >= 224 and ip[0] <= 239 then the IP address is in class D
        elif ip[0] >= 224 and ip[0] <= 239:
            return "D"
        
        # Otherwise the IP address is in Class E
        else:
            return "E"
    
    def format_ip(self):
        """
        Format the IP address to standard notation.
        :return: The formatted IP address.
        """
        try:
            parts = [str(int(part)) for part in self.IP.split('.')]
            return '.'.join(parts)
        except ValueError:
            return "Invalid IP"
    
    def ip_to_int(self):
        """
        Convert the IP address to an integer.
        :return: The integer representation of the IP address.
        """
        try:
            parts = [int(part) for part in self.IP.split('.')]
            return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]
        except ValueError:
            return None
    
    def is_reserved_ip(self):
        """
        Check if the IP address is a reserved IP address (private network).
        :return: True if the IP address is reserved, otherwise False.
        """
        if self.validate_it() != "Valid IPv4":
            return False
        
        ip_parts = [int(part) for part in self.IP.split('.')]
        # Check if the IP falls within the reserved ranges
        if (ip_parts[0] == 10) or \
           (ip_parts[0] == 172 and 16 <= ip_parts[1] <= 31) or \
           (ip_parts[0] == 192 and ip_parts[1] == 168):
            return True
        
        return False
    
    def delete_objects(self):
        """
        Function to delete itself.
        """
        del self
