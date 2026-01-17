import time
import sys

def animasi_proses(teks_input, hasil_output):
    sys.stdout.write(f"\r[MEMBUKA]: {teks_input} ---> {hasil_output}")
    sys.stdout.flush()
    time.sleep(random.uniform(0.05, 0.3))
def decrypt_program():
    palet = {
        "1": {"shift": 1}, "2": {"shift": 2}, "3": {"shift": 1},
        "4": {"shift": 2}, "5": {"shift": 1}, "6": {"shift": 2}
    }

    print("=== DEKRIPSI REAL-TIME ===")
    pesan_hangul = input("Masukkan pesan Hangul: ")
    kunci = input("Masukkan kunci urutan warna: ")

    hangul_offset = 0xAC00
    alfabet_asli = ""

    print("\nSedang membedah kode...")
    try:
        for i, char_hangul in enumerate(pesan_hangul):
            n_shift = palet[kunci[i % len(kunci)]]["shift"]
            posisi_asli = (ord(char_hangul) - hangul_offset) - n_shift
            char_asli = chr(posisi_asli)
            alfabet_asli += char_asli
            
            # Menjalankan animasi per karakter
            animasi_proses(pesan_hangul[:i+1], alfabet_asli)

        print(f"\n\nSelesai! Pesan Asli: {alfabet_asli}")
    except:
        print("\n\n[!] Error: Kunci atau pesan tidak valid.")

if __name__ == "__main__":
    decrypt_program()