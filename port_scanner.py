import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    url = ''
    try:
        url = socket.gethostbyaddr(target)
        url = url[0]
    except:
        pass
    try:
        host = socket.gethostbyname(target)
    except:
        try:
            int(target.replace('.', ''))
            return 'Error: Invalid IP address'
        except:
            return 'Error: Invalid hostname'
    port = port_range[0]
    open_ports = ''
    ports = []
    while port <= port_range[1]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((host, port)):
            pass
        else:
            ports.append(port)
        s.settimeout(None)
        port += 1
    if verbose:
        if url == '':
            open_ports += f'Open ports for {host}'
        else:
            open_ports += f'Open ports for {url} ({host})'
        open_ports += '\nPORT     SERVICE'
        for item in ports:
            open_ports += ('\n%-4s %-s %-s' %
                           (str(item), '   ', ports_and_services[item]))
    else:
        open_ports = ports
    return open_ports