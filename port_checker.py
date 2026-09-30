from scapy.all import IP, TCP, sr1

target = input("Target IP enter karein: ")
port = int(input("Port number enter karein: "))

pkt = IP(dst=target)/TCP(dport=port, flags="S")

response = sr1(pkt, timeout=2, verbose=0)

if response:
    if response.haslayer(TCP):
        if response.getlayer(TCP).flags == 18:  # SYN-ACK
            print("Port Open Hai!")
        else:
            print("Port Closed Hai!")
else:
    print("Port Filtered ya No Response!")
