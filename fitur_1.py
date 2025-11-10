import re


def hitung_BMI():
    def perhitungan_bmi(berat, tinggi_cm):
        tinggi_m = tinggi_cm / 100
        return berat / (tinggi_m ** 2)

    def kategori_bmi(bmi):
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi <= 24.9:
            return "Ideal"
        elif 25 <= bmi <= 29.9:
            return "Kelebihan berat badan"
        else:
            return "Obesitas"

    while True:
        print("\n=== PROGRAM HITUNG BMI ===")

        try:
            while True:
                berat = float(input("Masukkan berat badan (kg): "))
                if berat <= 0:
                    print("\nTidak sesuai dengan ketentuan! Berat harus lebih dari 0 kg.\n")
                    continue
                else:
                    break

            while True:
                tinggi = float(input("Masukkan tinggi badan (cm): "))
                if tinggi <= 0:
                    print("\nTidak sesuai dengan ketentuan! Tinggi harus lebih dari 0 cm.\n")
                    continue
                else:
                    break

            bmi = perhitungan_bmi(berat, tinggi)
            kategori = kategori_bmi(bmi)

            print("\n=== HASIL PERHITUNGAN BMI ===")
            print(f"Berat badan : {berat} kg")
            print(f"Tinggi badan: {tinggi} cm")
            print(f"Nilai BMI   : {bmi:.2f}")
            print(f"Kategori    : {kategori}")

            while True:
                ulang = input("\nIngin menghitung lagi? (y/n): ").lower()

                if not re.match(r"^(y|n)$", ulang):
                    print("\n❌ Format salah! Hanya boleh 'y' atau 'n'.")
                    continue
                else:
                    break

            if ulang != "y":
                break
            else:
                continue

        except ValueError:
            print("\n ⚠ INPUTAN HANYA BOLEH ANGKA ⚠\n")