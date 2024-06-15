import nmap

def scan_network(ip_range, ports):
    nm = nmap.PortScanner()
    nm.scan(ip_range, ports)
    results = []
    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            'ports': []
        }
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                host_info['ports'].append({
                    'port': port,
                    'state': nm[host][proto][port]['state']
                })
        results.append(host_info)
    return results
