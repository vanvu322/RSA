import rsa_functions as rsa
import random

# Hàm để sinh số nguyên tố ngẫu nhiên có độ dài chữ số cho trước
def generate_prime_candidate(length):
    start = 10**(length - 1)
    end = 10**length - 1
    while True:
        candidate = random.randint(start, end)
        if rsa.is_prime(candidate):
            return candidate

def main():
    # Nhập độ dài số chữ số cho p và q từ người dùng
    length = int(input("Nhập độ dài số chữ số cho p và q: "))

    # Sinh số nguyên tố p và q với độ dài cho trước
    p = generate_prime_candidate(length)
    q = generate_prime_candidate(length)

    # Tạo một thông điệp mẫu
    message = "Hello RSA!"

    # In các giá trị này ra terminal
    print(f"Các thông số đã được sinh ra:\n p = {p}\n q = {q}\n message = {message}")

if __name__ == "__main__":
    main()
