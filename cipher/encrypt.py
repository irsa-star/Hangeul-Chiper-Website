import time
import sys
import random

def animasi_proses(teks_input, hasil_output):
    # Mengupdate baris yang sama di terminal
    sys.stdout.write(f"\r[MENGUNCI]: {teks_input} ---> {hasil_output}")
    sys.stdout.flush()
    time.sleep(random.uniform(0.05, 0.3))

def encrypt_program():
    palet = {
        "1": {"nama": "Merah",  "shift": 1},
        "2": {"nama": "Hijau",  "shift": 2},
        "3": {"nama": "Biru",   "shift": 1},
        "4": {"nama": "Kuning", "shift": 2},
        "5": {"nama": "Ungu",   "shift": 1},
        "6": {"nama": "Cyan",   "shift": 2}
    }

    print("=== ENKRIPSI REAL-TIME ===")
    kunci = input("Pilih urutan warna (1-6): ")
    plaintext = input("Masukkan pesan alfabet: ")

    hangul_offset = 0xAC00
    hasil_hangul = ""
    
    print("\nSedang memproses...")
    for i, char in enumerate(plaintext):
        n_shift = palet[kunci[i % len(kunci)]]["shift"]
        char_hangul = chr(hangul_offset + ord(char) + n_shift)
        hasil_hangul += char_hangul
        
        # Menjalankan animasi per karakter
        animasi_proses(plaintext[:i+1], hasil_hangul)

    print(f"\n\nSelesai! Hasil Akhir: {hasil_hangul}")

if __name__ == "__main__":
    encrypt_program()