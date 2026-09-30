from scapy.all import IP, ICMP, sr1

target = input("Target IP enter karein: ")
pkt = IP(dst=target)/ICMP()

response = sr1(pkt, timeout=2, verbose=0)

if response:
    print("Host Online Hai!")
else:
    print("Host Offline Hai!")
