import nmap

def scan_network(ip_range, ports, scan_type):
    nm = nmap.PortScanner()

    if scan_type == 'quick':
        arguments = '-T4 -F'
    elif scan_type == 'full':
        arguments = '-T4 -A -v'
    elif scan_type == 'vuln':
        arguments = '--script vuln'
    else:
        arguments = '-T4 -F'

    nm.scan(ip_range, ports, arguments=arguments)

    results = []
    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            'mac': nm[host]['addresses'].get('mac'),
            'vendor': nm[host]['vendor'],
            'ports': [
                {'port': port, 'state': nm[host][proto][port]['state']}
                for proto in nm[host].all_protocols()
                for port in nm[host][proto].keys()
            ]
        }
        results.append(host_info)
    return results
