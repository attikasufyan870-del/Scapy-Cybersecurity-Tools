import socket

# Target IP define karein (localhost)
target_ip = "127.0.0.1"

# Check karne ke liye ports ki list
ports_to_scan = [22, 80, 443]

print(f"[*] Scanning started on target: {target_ip}")

for port in ports_to_scan:
    try:
        # Socket object create karein (IPv4 aur TCP ke liye)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # 1 second ka timeout taake script ruke na
        
        # Port par connect hone ki koshish
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
            
        # Socket close kar dein
        s.close()
        
    except Exception as e:
        print(f"[-] Error on port {port}: {e}")

print("[*] Scanning finished.")
