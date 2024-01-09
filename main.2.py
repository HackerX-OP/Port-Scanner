import socket
import threading

tar = input("Enter the domain of target: ")

def port_scan(host, port):
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(2)

    result = a.connect_ex((host, port))
    if result == 0:
        try:
            service_name = socket.getservbyport(port)
            print(f"Port {port} open - Service: {service_name}")
        except:
            pass
    else:
        print(f"Port {port} closed")

    a.close()

def threaded_port_scans(host):
    threads = []

    for port in range(1, 1001):
        thread = threading.Thread(target=port_scan, args=(host, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

threaded_port_scans("bostonpublicschoolagra.com")
