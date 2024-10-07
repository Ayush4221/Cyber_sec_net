import ipaddress 

def range_checker(ip: str, subnet: str ) -> bool:
   
    
    network = ipaddress.ip_network(f'{ip}/{subnet}', strict=False) 
    print(network)
    return ipaddress.ip_address(ip) in network 

print(range_checker('192.168.10.0', '255.255.255.0')) 
    
