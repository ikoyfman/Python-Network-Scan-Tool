# This script runs on Python 3
import socket
import threading
from multiprocessing import Pool, Process
import time


def tcp_connect(ip, port_number):
    try:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(0.1)
        scanner.connect((str(ip), port_number))
        scanner.close()
        return True
    except:
        return False


def scan_ports(host_ip, port_start, port_end):
    results = {}

    if port_start and port_end is None:
        connection_result = tcp_connect(host_ip, port_start)
        results[port_start] = connection_result

    # Prepare list to capture port ranges for multiple ports
    if port_start != port_end and port_end is not None:
        port_ranges = []
        for ports in range(port_start, port_end + 1):
            port_ranges.append(ports)
        results = port_scan_threader(host_ip, port_ranges)

    return results


def _multiprocess_port_scan_helper(param):
    host_ip = param[0]
    port_numb = param[1]
    return tcp_connect(host_ip, port_numb)


def port_scan_threader(host_ip, port_range):
    host_ports = []
    for numb in port_range:
        host_ip_port = [host_ip, numb]
        host_ports.append(host_ip_port)
    
    host_chunks = [host_ports[host:host+20] for host in range(0,len(host_ports),20)]
    for chunk in host_chunks:
        for host in chunk:
            p = Process(target=_multiprocess_port_scan_helper, args(host,))
            p.start()
            p.join()
#     p = Pool()
#     result_list = p.map(_multiprocess_port_scan_helper, host_ports)
#     p.close()

#     port_dict = {}
#     for idx, result in enumerate(result_list):
#         port_dict[idx + 1] = result_list[idx]

    return port_dict


if __name__ == "__main__":
    assert tcp_connect("google.com", 80) is True
    assert tcp_connect("google.com", 53) is False

    results = scan_ports("google.com", 1, 500)
    assert results[443] is True
    assert results[80] is True
    assert results[500] is False
