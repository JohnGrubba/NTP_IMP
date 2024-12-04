import socket
import struct
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("0.0.0.0", 42069)
print("Starting up on {} port {}".format(*server_address))
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(1024)

    # We just don't care about the data, we just want to send the time

    if data:
        print(
            "Received EJTP (Elias Jonas Time Protocol) Request from {}".format(
                address[0]
            )
        )
        t2 = time.time()
        # Simulate server processing time
        time.sleep(0.327)
        t3 = time.time()
        data = struct.pack("!2d", t2, t3)
        sock.sendto(data, address)
