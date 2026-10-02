# Step 1: Tool ko bulana (Library import karna)
from cryptography.fernet import Fernet

# Step 2: Pehle taala aur chabi (Key) banana zaroori hai
my_key = Fernet.generate_key()

# Step 3: Us chabi ko encryption machine mein dalna
cipher_machine = Fernet(my_key)


secret_text = "Yeh mera confidential data hai!"
print("Asli Message:", secret_text)

# Step 5: Message ko bytes mein convert kar ke lock (encrypt) karna
encrypted_data = cipher_machine.encrypt(secret_text.encode())
print("Lock Huwa Data (Ciphertext):", encrypted_data)

# Step 6: Wapis usi chabi se message ko kholna (decrypt) karna
decrypted_data = cipher_machine.decrypt(encrypted_data)

# Step 7: Bytes ko wapis aam parhne wali text (string) mein badalna
final_text = decrypted_data.decode()
print("Wapis Khula Message:", final_text)
