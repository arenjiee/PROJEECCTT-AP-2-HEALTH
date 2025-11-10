
def tanya_gejala(daftar_pertanyaan):
    total = 0

    for p in daftar_pertanyaan:
        print("\n" + p)

        # Input frekuensi
        while True:
            frek_input = input("  Frekuensi (0=tidak pernah, 1=kadang, 2=sering, ketik 'exit' untuk keluar): ")

            # Jika pengguna ingin keluar
            if frek_input == "exit":
                print("Terima kasih! Program dihentikan.")
                return None

            # Pastikan input angka valid
            if frek_input.isdigit():
                frek = int(frek_input)
                if frek in [0, 1, 2]:
                    break
                else:
                    print("Masukkan hanya angka 0, 1, atau 2!")
            else:
                print("Harus berupa angka atau ketik 'exit' untuk keluar!")

        # Jika frekuensi = 0 → lanjut ke pertanyaan berikutnya
        if frek == 0:
            continue

        # Input intensitas
        while True:
            inten_input = input("  Intensitas (1=ringan, 2=berat, ketik 'exit' untuk keluar): ")

            if inten_input == "exit":
                print("Terima kasih! Program dihentikan.")
                return None

            if inten_input.isdigit():
                inten = int(inten_input)
                if inten in [1, 2]:
                    break
                else:
                    print("Masukkan hanya angka 1 atau 2!")
            else:
                print("Harus berupa angka atau ketik 'exit' untuk keluar!")

        # Hitung skor pertanyaan ini
        skor = frek * inten
        total += skor
        
    return total

def kategori_cvs(total):
    if total == 0:
        return "Tidak ada gejala CVS"
    elif total <= 6:
        return "Tidak ada CVS"
    elif total <= 13:
        return "CVS ringan"
    else:
        return "CVS sedang/berat"

def main():
    pertanyaan = [
        "1. Penglihatan kabur saat melihat jauh",
        "2. Penglihatan kabur saat melihat dekat",
        "3. Penglihatan ganda",
        "4. Mata terasa terbakar",
        "5. Mata terasa gatal",
        "6. Mata terasa berat",
        "7. Nyeri di sekitar mata",
        "8. Mata merah",
        "9. Mata berair",
        "10. Mata terasa kering",
        "11. Sakit kepala",
        "12. Sakit leher atau bahu",
        "13. Silau terhadap cahaya",
        "14. Sulit fokus",
        "15. Seperti ada benda asing di mata",
        "16. Rasa tidak nyaman di mata"
    ]

    print("=== KUESIONER COMPUTER VISION SYNDROME (CVS-Q) ===")
    print("Frekuensi: 0=Tidak Pernah | 1=Kadang-kadang | 2=Sering")
    print("Intensitas: 1=Ringan | 2=Berat")
    print("Ketik 'exit' kapan saja untuk keluar dari program.")

    nama = input("Masukkan nama Anda (atau ketik 'exit' untuk keluar): ")
    if nama == "exit":
        print("Terima kasih! Program dihentikan.")
        return

    total_skor = tanya_gejala(pertanyaan)

    # Jika pengguna keluar di tengah jalan
    if total_skor is None:
        return

    hasil = kategori_cvs(total_skor)

    print("=== HASIL PENILAIAN CVS ===")
    print("Nama:", nama)
    print("Total Skor:", total_skor)
    print("Kategori:", hasil)

# Jalankan program
main()