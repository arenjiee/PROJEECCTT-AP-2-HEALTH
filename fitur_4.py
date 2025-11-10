import database_set
import re

daftar_workout = ["push up", "sit up", "plank", "squat", 
        "pull up", "jogging", "jumping jack", 
        "burpee", "yoga",
    ]

def fitur_4():
    def set_target():
        while True:
            print("\n=== SET TARGET HARIAN ===\n")
            print("1. 💪 Workout")
            print("2. 🔥 Kalori")
            print("3. 🥩 Protein")
            print("4. 👋 Keluar")

            try:
                pilihan = int(input("Pilih Target yang di set (1/2/3): "))

                if pilihan == 1:
                    while True:
                        print("\n=== 💪 PILIH WORKOUT HARI INI ===\n")
                        for i in daftar_workout:
                            print(f"- {i.title()}")

                        workout = (input("Masukkan target workout : ").strip().lower())

                        pattern = r"^([a-zA-Z ]+)\s+(\d+)\s*(x|menit|m)?$"
                        match = re.match(pattern, workout)

                        if not match:
                            print("\n❌ Format salah! Gunakan format seperti 'push up 30x' atau 'plank 2 menit'.\n")
                            continue
                        
                        nama_workout = match.group(1).strip().lower()
                        jumlah = match.group(2)
                        satuan = match.group(3) if match.group(3) else ""

                        if nama_workout not in daftar_workout:
                            print(f"\n⚠️ '{nama_workout}' tidak ada di daftar workout yang tersedia.\n")
                            continue
                        
                        workout_db = database_set.get_workouts()
                        workout_nama = [' '.join(w[1].split()[:-1]).lower() for w in workout_db]

                        if nama_workout in workout_nama:
                            print(f"\n❌ Target {nama_workout} telah di set sebelumnya!!")
                            break

                        if satuan == "x":
                            full_workout = f"{nama_workout} {jumlah}{satuan}"
                        elif satuan == "menit":
                            full_workout = f"{nama_workout} {jumlah} {satuan}"
                        else:
                            full_workout = f"{nama_workout} {jumlah} {satuan}"

                        database_set.insert_target_workout(full_workout)
                        print(f"\n✅ Target '{full_workout}' berhasil disimpan !\n")

                        while True:
                            lanjut = input("Apakah masih ada workout yang ingin di set? (y/n): ").strip().lower()

                            if not re.match(r"^(y|n)$", lanjut):
                                print("\n❌ Format salah! Hanya boleh 'y' atau 'n'.\n")
                                continue
                            else:
                                break

                        if lanjut != "y":
                            break
                        else:
                            continue
                
                elif pilihan == 2:
                    kalori = int(input("Masukkan target kalori harian (kkal): "))
                    database_set.insert_target_kalori(kalori)
                    print("\n✅ Target kalori berhasil disimpan !!")
                elif pilihan == 3:
                    protein = int(input("Masukkan target protein harian (gram): "))
                    database_set.insert_target_protein(protein)
                    print("\n✅ Target protein berhasil disimpan !!")
                elif pilihan == 4:
                    break
                else:
                    print("💢 Pilihan tidak ada di menu")
            except ValueError:
                print("\n ⚠️ INPUTAN HANYA BOLEH ANGKA ⚠️\n")

        print("\n✅ Target baru berhasil disimpan, semangat berjuang !!\n")

    def hapus_workout():
        workouts = database_set.get_workouts()

        if not workouts:
            print("\n❌ Tidak ada workout yang bisa dihapus.\n")
            return

        print("\n=== HAPUS WORKOUT ===")
        for i, w in enumerate(workouts, 1):
            print(f"{i}. {w[1]}")   # Tampilkan tanpa ID

        try:
            nomor = int(input("\nMasukkan nomor workout yang ingin dihapus: "))

            # Validasi rentang nomor
            if nomor < 1 or nomor > len(workouts):
                print("❌ Nomor tidak valid.\n")
                return

            # Ambil ID dari workout berdasarkan index
            workout_id = workouts[nomor - 1][0]

            database_set.delete_workout_by_id(workout_id)
            print("✅ Workout berhasil dihapus!\n")

        except ValueError:
            print("❌ Input harus berupa angka.\n")


    def lihat_target():
        print("\n=== TARGET SAAT INI ===")
        target = database_set.get_target()

        if target is None:
            print("❌ Belum ada target kalori/protein.")
            return

        kalori, protein = target
        workouts = database_set.get_workouts()

        print("\n-- Workout yang Ditargetkan --")
        if workouts:
            for i, w in enumerate(workouts, 1):
                print(f"{i}. {w[1]}")
        else:
            print("💢 Belum ada workout ditambahkan.")

        print(f"\nKalori  : {kalori} kkal")
        print(f"Protein : {protein} gram\n")
        
    while True:
        print("\n=== MENU SET TARGET HARIAN ===\n")
        print("1. 🎯 Set Target Harian")
        print("2. 📊 Lihat Target Tersimpan")
        print("3. 🧹 Hapus workout")
        print("4. 👋 Keluar")

        try:
            pilihan_menu= int(input("Pilih menu (1-3): "))
            if pilihan_menu == 1:
                set_target()
            elif pilihan_menu == 2:
                lihat_target()
            elif pilihan_menu == 3:
                hapus_workout()
            elif pilihan_menu == 4:
                print("🎉🎉 Program selesai. 🎉🎉")
                break
            else:
                print("💢 Pilihan tidak ada di menu")
        except ValueError:
            print("\n⚠️ INPUTAN HANYA BOLEH ANGKA ⚠️\n")
            continue