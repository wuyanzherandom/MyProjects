import urllib
import json
import socket


"verify ipv4"
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


"verify ipv6"
def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


class IPAPI:
    """
    description:
    information check https://ipapi.co/api/
    """

    url = "https://ipapi.co/"

    formats_list = [
        'json',
        'jsonp',
        'xml',
        'csv',
        'yaml',
    ]

    "get geolocation from given ip"
    def getip(self, ip, formats='json'):
        if formats in self.formats_list:
            flag = is_valid_ipv4_address(ip)
            if flag:
                url = self.url + ip + "/" + formats + "/"
                response = urllib.urlopen(url)
                return True, '', json.loads(response.read())
            else:
                return False, msg, ''
        else:
            return False, 'formats not in the formats lists' ,None
