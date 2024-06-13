import tkinter as tk
from tkinter import messagebox
import rsa_functions as rsa

def generate_keys():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        public, private = rsa.generate_keypair(p, q)
        entry_public_key.delete(0, tk.END)
        entry_private_key.delete(0, tk.END)
        entry_public_key.insert(0, str(public))
        entry_private_key.insert(0, str(private))
        messagebox.showinfo("Thành công", "Khóa công khai và khóa bí mật đã được tạo!")
    except ValueError as e:
        messagebox.showerror("Lỗi", str(e))

def encrypt_message():
    try:
        public_key = eval(entry_public_key.get())
        message = entry_message.get()
        encrypted_msg = rsa.encrypt(public_key, message)
        encrypted_str = ' '.join(map(str, encrypted_msg))
        entry_encrypted.delete(0, tk.END)
        entry_encrypted.insert(0, encrypted_str)
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

def decrypt_message():
    try:
        private_key = eval(entry_private_key.get())
        encrypted_str = entry_encrypted.get()
        encrypted_msg = list(map(int, encrypted_str.split()))
        decrypted_msg = rsa.decrypt(private_key, encrypted_msg)
        entry_decrypted.delete(0, tk.END)
        entry_decrypted.insert(0, decrypted_msg)
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))

# Tạo cửa sổ chính
root = tk.Tk()
root.title("RSA Encryption/Decryption")

# Nhãn và ô nhập cho số nguyên tố p
label_p = tk.Label(root, text="Số nguyên tố (p):")
label_p.grid(row=0, column=0, padx=10, pady=5)
entry_p = tk.Entry(root)
entry_p.grid(row=0, column=1, padx=10, pady=5)

# Nhãn và ô nhập cho số nguyên tố q
label_q = tk.Label(root, text="Số nguyên tố (q):")
label_q.grid(row=1, column=0, padx=10, pady=5)
entry_q = tk.Entry(root)
entry_q.grid(row=1, column=1, padx=10, pady=5)

# Nút để tạo khóa
btn_generate = tk.Button(root, text="Tạo khóa", command=generate_keys)
btn_generate.grid(row=2, column=0, columnspan=2, pady=10)

# Nhãn và ô nhập cho khóa công khai
label_public_key = tk.Label(root, text="Khóa công khai:")
label_public_key.grid(row=3, column=0, padx=10, pady=5)
entry_public_key = tk.Entry(root, width=50)
entry_public_key.grid(row=3, column=1, padx=10, pady=5)

# Nhãn và ô nhập cho khóa bí mật
label_private_key = tk.Label(root, text="Khóa bí mật:")
label_private_key.grid(row=4, column=0, padx=10, pady=5)
entry_private_key = tk.Entry(root, width=50)
entry_private_key.grid(row=4, column=1, padx=10, pady=5)

# Nhãn và ô nhập cho thông điệp cần mã hóa
label_message = tk.Label(root, text="Thông điệp:")
label_message.grid(row=5, column=0, padx=10, pady=5)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=5, column=1, padx=10, pady=5)

# Nút để mã hóa thông điệp
btn_encrypt = tk.Button(root, text="Mã hóa", command=encrypt_message)
btn_encrypt.grid(row=6, column=0, columnspan=2, pady=10)

# Nhãn và ô nhập cho thông điệp đã mã hóa
label_encrypted = tk.Label(root, text="Thông điệp đã mã hóa:")
label_encrypted.grid(row=7, column=0, padx=10, pady=5)
entry_encrypted = tk.Entry(root, width=50)
entry_encrypted.grid(row=7, column=1, padx=10, pady=5)

# Nút để giải mã thông điệp
btn_decrypt = tk.Button(root, text="Giải mã", command=decrypt_message)
btn_decrypt.grid(row=8, column=0, columnspan=2, pady=10)

# Nhãn và ô nhập cho thông điệp đã giải mã
label_decrypted = tk.Label(root, text="Thông điệp đã giải mã:")
label_decrypted.grid(row=9, column=0, padx=10, pady=5)
entry_decrypted = tk.Entry(root, width=50)
entry_decrypted.grid(row=9, column=1, padx=10, pady=5)

# Bắt đầu vòng lặp chính của Tkinter
root.mainloop()
