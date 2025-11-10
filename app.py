import fitur_4, fitur_3, fitur_2, fitur_6, fitur_1, fitur_5, fitur_7
import show

def main():
    show.greeting()
    while True:
        show.menu()
        try:     
            pilihan = int(input("Pilih Menu (1-8): "))

            if pilihan == 1:
                fitur_1.hitung_BMI()

            elif pilihan == 2:
                fitur_2.fitur_2()

            elif pilihan == 3:
                fitur_3.healthcheck()
            
            elif pilihan == 4:
                fitur_4.fitur_4()
            
            elif pilihan == 5:
                fitur_5.fitur_5()
            
            elif pilihan == 6:
                fitur_6.cek_mood()
            
            elif pilihan == 7:
                fitur_7.main()
                
            elif pilihan == 8:
                print("\nPROGRAM BERHENTI")
                exit()
            else:
                print("Pilihan tidak ada di menu")

        except ValueError:
            print("\n ⚠️ INPUTAN HANYA BOLEH ANGKA ⚠️\n")
            

if __name__ == "__main__":
    main()