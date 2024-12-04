import socket
import struct
import time
from numpy import array

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("172.31.182.70", 42069)


def perform_sync() -> float:
    t1 = time.time()
    message = b"EJTP (Elias Jonas Time Protocol) request"
    sock.sendto(message, server_address)

    print("Waiting for server...")
    data, _ = sock.recvfrom(4096)
    t2, t3 = struct.unpack("!2d", data)
    t4 = time.time()

    network_latency_avg = ((t4 - t1) - (t3 - t2)) / 2
    print("Network Latency: ", network_latency_avg)
    server_processing_time = t3 - t2
    print("Server Processing Time: ", server_processing_time)
    actual_time = t3 + network_latency_avg
    client_time = time.time()
    print("Server Time: {0} | Client Time: {1}".format(actual_time, client_time))
    print("Time Difference: ", actual_time - client_time)
    return actual_time - client_time


# Perform the sync 10 times (for better accuracy)
time_diffs = [perform_sync() for _ in range(10)]
print("Average Time Difference: ", sum(time_diffs) / len(time_diffs))
print("Standard Deviation: ", array(time_diffs).std())
