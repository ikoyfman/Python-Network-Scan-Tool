from .network_scanning import network_scan, get_hostname
from .port_scanner_threading import tcp_connect, scan_ports


class Network(object):
    def __init__(self, ipaddress, subnet=None):
        self.ipaddress = ipaddress
        self.subnet = str(subnet)
        self.hosts = []

    def discover_hosts(self):
        results = network_scan(self.ipaddress, self.subnet)
        for ipaddr, value in results.items():
            if value:
                self.hosts.append(Host(ipaddr))

    def discover_ports_hosts(self):
        for ip_host in self.hosts:
            ip_host.scan_host_ports()

    def discover_hostnames(self):
        for ip_host in self.hosts:
            ip_host.get_hostname()


class Host(object):

    def __init__(self, ipaddress):
        self.ipaddress = ipaddress

    def __repr__(self):
        return self.ipaddress

    def scan_host_ports(self, port_start=1, port_end=1024):
        results = scan_ports(self.ipaddress, port_start, port_end)
        self.open_ports = results

    def get_hostname(self):
        result = get_hostname(self.ipaddress)
        self.hostname = result
