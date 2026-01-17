# cipher/core.py
import re

# ==========================
# DATABASE KUNCI WARNA (PATEN)
# ==========================
COLOR_DATABASE = {
    '1': {"hex": "#2F3E46", "shift": 2},
    '2': {"hex": "#1C1C1C", "shift": 1},
    '3': {"hex": "#4A4E69", "shift": 2},
    '4': {"hex": "#3A5A40", "shift": 1},
    '5': {"hex": "#6D597A", "shift": 2},
    '6': {"hex": "#22223B", "shift": 1}
}

# ==========================
# MAP ALFABET ↔ HANGEUL
# ==========================
HANGEUL_MAP = {
    'A': '가', 'B': '나', 'C': '다', 'D': '라', 'E': '마', 'F': '바',
    'G': '사', 'H': '아', 'I': '자', 'J': '차', 'K': '카', 'L': '타',
    'M': '파', 'N': '하', 'O': '거', 'P': '너', 'Q': '더', 'R': '러',
    'S': '머', 'T': '버', 'U': '서', 'V': '어', 'W': '저', 'X': '처',
    'Y': '커', 'Z': '터'
}
REVERSE_MAP = {v: k for k, v in HANGEUL_MAP.items()}

MAX_CHARS = 200


# ==========================
# ENKRIPSI v3.1 (FIXED)
# ==========================
def encrypt_v3(plaintext: str, key_choice: str) -> str:
    if not plaintext or len(plaintext) > MAX_CHARS:
        raise ValueError("Input kosong atau terlalu panjang")

    if not key_choice or not all(c in COLOR_DATABASE for c in key_choice):
        raise ValueError("Kunci warna tidak valid")

    plaintext = plaintext.upper()
    shifts = [COLOR_DATABASE[c]['shift'] for c in key_choice]
    hexs = [COLOR_DATABASE[c]['hex'] for c in key_choice]

    result = []
    key_index = 0  # 🔑 hanya maju saat karakter dienkripsi

    for char in plaintext:
        if 'A' <= char <= 'Z':
            idx = key_index % len(shifts)
            shift = shifts[idx]
            hex_val = hexs[idx]

            shifted_idx = (ord(char) - ord('A') + shift) % 26
            shifted_char = chr(shifted_idx + ord('A'))
            hangeul_char = HANGEUL_MAP[shifted_char]

            result.append(f"[{hex_val}] {hangeul_char}")
            key_index += 1
        else:
            # Spasi / simbol tidak mempengaruhi key
            result.append(char)

    return " ".join(result)


# ==========================
# DEKRIPSI v3.1 (FIXED)
# ==========================
def decrypt_v3(ciphertext: str, key_choice: str) -> str:
    if not key_choice or not all(c in COLOR_DATABASE for c in key_choice):
        raise ValueError("Kunci warna tidak valid")

    shifts = [COLOR_DATABASE[c]['shift'] for c in key_choice]

    # Pisahkan [HEX] dan karakter
    parts = re.findall(r'(\[[^\]]+\]\s)?([^\s\[\]]+)', ciphertext)

    decoded_result = ""
    key_index = 0  # 🔑 sinkron dengan enkripsi

    for _, char in parts:
        if char in REVERSE_MAP:
            idx = key_index % len(shifts)
            shift = shifts[idx]

            alpha_char = REVERSE_MAP[char]
            original_idx = (ord(alpha_char) - ord('A') - shift) % 26
            decoded_result += chr(original_idx + ord('A'))

            key_index += 1
        else:
            decoded_result += char

    return decoded_result
