import random

# Hàm tính ước chung lớn nhất của hai số
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tìm nghịch đảo modulo của e và phi
def mod_inverse(e, phi):
    d = 0
    x1, x2, x3 = 1, 0, phi
    y1, y2, y3 = 0, 1, e
    
    while y3 != 0:
        q = x3 // y3
        t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
        x1, x2, x3 = y1, y2, y3
        y1, y2, y3 = t1, t2, t3
    if x2 < 0:
        x2 += phi
    return x2

# Hàm kiểm tra một số có phải là số nguyên tố hay không
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Hàm tạo cặp khóa công khai và khóa bí mật
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Cả hai số phải là số nguyên tố.')
    elif p == q:
        raise ValueError('p và q không thể bằng nhau')
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

# Hàm mã hóa thông điệp bằng khóa công khai
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

# Hàm giải mã thông điệp bằng khóa bí mật
def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)
