import paramiko

# 1. Target details
host = "192.168.1.100"  # Target Server IP
username = "ubuntu"
password = "your_password"

# 2. SSH Client create aur configure karein
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"[*] Connecting to {host}...")
    # 3. Connection establish karein
    ssh.connect(hostname=host, username=username, password=password, timeout=5)
    print("[+] Connection successful!")

    # 4. Command run karein (jaise system info dekhna)
    stdin, stdout, stderr = ssh.exec_command("uname -a")
    
    # Output read aur print karein
    output = stdout.read().decode()
    print("[*] Command Output:")
    print(output)

except Exception as e:
    print(f"[-] Connection failed: {e}")

finally:
    # 5. Connection close karein
    ssh.close()
    print("[*] SSH connection closed.")
