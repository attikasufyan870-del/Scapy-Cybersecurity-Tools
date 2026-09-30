from scapy.all import Ether, ARP, srp

target = input("Network range enter karein (misal ke taur par 192.168.100.0/24): ")
arp = ARP(pdst=target)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
pkt = ether/arp

result = srp(pkt, timeout=2, verbose=0)[0]

print("IP Address\t\tMAC Address")
print("-" * 40)
for sent, received in result:
    print(f"{received.psrc}\t\t{received.hwsrc}")
