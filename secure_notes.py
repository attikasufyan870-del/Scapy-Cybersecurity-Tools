from cryptography.fernet import Fernet

my_key = Fernet.generate_key()

cipher_machine = Fernet(my_key)

secret_text = "My personal banking credentials are safe."
print("Asli message:",secret_text)

encrypted_data = cipher_machine.encrypt(secret_text.encode())
print("Lock Howa Data(ciphertext):" , encrypted_data)

decrypted_data = cipher_machine.decrypt(encrypted_data)

final_text = decrypted_data.decode()
print("Wapies khula message:" , final_text)
