import socket

for ping in range(1,254):
    addresse="100.113.38." + str(ping)
    socket.setdefaulttimeout(2)
    
    try:
        hostname, alias, addresslist = socket.gethostbyaddr(addresse)
        
    except socket.herror:
        hostname=None
        alias=None
        addresslist=addresse
    print(addresslist, '→',  hostname)