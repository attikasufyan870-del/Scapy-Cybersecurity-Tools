from cryptography.fernet import Fernet

my_key = Fernet.generate_key()

cipher_machine = Fernet(my_key)

secret_text = "Admin@Wifi#2026"
print("Asli message:" , secret_text)

encrypted_data = cipher_machine.encrypt(secret_text.encode())
print("Lock Howa Data(ciphertext):" , encrypted_data)

decrypted_data = cipher_machine.decrypt(encrypted_data)

final_text = decrypted_data.decode()
print("Wapies Khula Data:" , final_text)
