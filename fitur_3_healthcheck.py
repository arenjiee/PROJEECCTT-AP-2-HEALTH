def healthcheck():
    print("\n=== 🔍🔍 HealthCheck 🔍🔍 ===")
    print("Cek kesehatan berdasarkan kegiatan harianmu!!\n")

    while True:
        try:
            usia = int(input("Masukkan usia (tahun): "))
            if usia <= 0:
                print("⚠ Usia tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk usia.\n")

    while True:
        try:
            tidur = int(input("Masukkan durasi tidur (jam): "))
            if tidur <= 0:
                print("⚠ Durasi tidur tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk durasi tidur.\n")

    while True:
        try:
            air_float = input("Masukkan jumlah air yang diminum hari ini (liter): ").replace(",", ".")
            air = float(air_float)
            if air <= 0:
                print("⚠ Jumlah konsumsi air tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk jumlah konsumsi air.\n")

    while True:
        try:
            olahraga = int(input("Masukkan durasi olahraga hari ini (menit): "))
            if olahraga <= 0:
                print("⚠ Durasi olahraga tidak valid! Masukkan angka lebih dari 0.\n")
                continue
            break
        except ValueError:
            print("⚠ Masukkan angka yang valid untuk durasi olahraga.\n")


    print("\n=== 📝 Ringkasan Kegiatan Hari Ini ===")
    print(f"Usia kamu: {usia} tahun")
    print(f"Durasi tidur: {tidur} jam")
    print(f"Asupan air harian: {air} liter")
    print(f"Durasi olahraga: {olahraga} menit\n")

    #tidur
    if 1 <= usia <= 5:
        print("🍼 Untuk usia 1–5 tahun, kebutuhan tidur bisa berbeda tiap anak.")
        print("👉 Disarankan konsultasi ke dokter anak untuk pola tidur yang sesuai yaa 💕")
    elif 6 <= usia <= 17:
        if tidur < 8:
            print("😴 Kamu kelihatan kurang tidur, coba tidur lebih awal lagi yaa malam ini!! 😉")
        elif 8 <= tidur <= 10:
            print("🌙 Tidurmu pas banget! Keren!! Terus jaga pola tidur kayak gini, okaayy? 😽")
        else:
            print("🫠 Tidurmu agak kebanyakan, takutnya malah bikin badan kerasa berat 😔, jangan terlalu sering yaa!!")
    elif 18 <= usia <= 59:
        if tidur < 7:
            print("💤 Tidurmu kurang dari ideal nih, usahain buat tidur sekitar 7–9 jam biar sehat, segar dan bugaarr!! 💪🏻")
        elif 7 <= tidur <= 9:
            print("🤩 MANTAF! Tidurmu udah cukup dan pas banget, pertahanin yakk!")
        else:
            print("😪 Tidur kelamaan juga nggak bagus, coba mulai bangun lebih awal lagii yaaa?")
    else:  #untuk lansia
        if tidur < 7:
            print("💤 Kurang tidur bisa bikin tubuh cepat lelah loh, usahain sekitar 7–8 jam yaa 😴")
        elif 7 <= tidur <= 8:
            print("🌙 Pas banget! Tidurmu cukup dan seimbang untuk lansia 👍🏻")
        else:
            print("😪 Tidur terlalu lama bisa ganggu ritme tubuhmu, coba kurangi sedikit yaa!")

    #air
    if 1 <= usia <= 5:
        print("🍼 Untuk anak usia 1–5 tahun, kebutuhan air tergantung berat badan dan aktivitas.")
        print("👉 Konsultasikan dengan dokter anak biar tahu jumlah cairan yang pas yaa 💧")
    elif air < 1.5:
        print("💧 Kamu kurang minum hari inii... 😔 Minum lagi biar ngga dehidrasi yaa!")
    elif 1.5 <= air <= 2.5:
        print("🥤 Bagus bangett! Asupan airmu pas, pertahankan!")
    else:
        print("🚰 HEY, HARI INI KAMU MINUMNYA KEBANYAKAN! Jangan berlebihan! Kasihan ginjalmu :(((")

    #olahraga
    if 1 <= usia <= 5:
        print("🤸‍♂ Untuk anak usia 1–5 tahun, aktivitas fisik sebaiknya diarahkan melalui bermain aktif!")
        print("👉 Tapi kalau mau tahu durasi tepatnya, sebaiknya konsultasi ke dokter anak yaa 🩺")
    elif 6 <= usia <= 17:
        if olahraga < 60:
            print("🏃‍♀ Olahraga kamu masii kurengg deh! Usahain olahraga minimal 60 menit sehari ya ya ya?")
        elif 60 <= olahraga <= 90:
            print("🔥 Keren banget banget! Durasi olahragamu udah pas banget untuk hari ini!!! 😻😻😻")
        elif 90 < olahraga <= 120:
            print("💪 Gacor! Kamu aktif banget hari ini, tapi jangan lupa untuk istirahat juga yaaww.")
        else:
            print("⚠ Eits, kamu olahraga lama banget, lebih dari 120 menit! Take a rest duluu please.")
    elif 18 <= usia <= 59:
        if olahraga < 30:
            print("🏃 Ehh! Jangan mager! Coba sempatin olahraga minimal 30 menit sehari okay? 😉.")
        elif 30 <= olahraga <= 60:
            print("Durasi olahragamu udah pas dan seimbang hari ini. Bagus bangett ⭐⭐⭐")
        elif 60 < olahraga <= 120:
            print("🔥 GG! Olahragamu cukup seimbang hari ini. Pertahankan!")
        else:
            print("⚠ Lebih dari 120 menit olahraga bisa bikin tubuh kelelahan, jangan terlalu dipaksaa yaaa!")
    else:  #untuk lansia
        if olahraga < 30:
            print("🚶‍♂ Sedikit bergerak tiap hari udah bagus kok, tapi usahain 30 menit biar tubuh tetap bugar 💪🏻")
        elif 30 <= olahraga <= 60:
            print("👏 Pas banget! Aktivitasmu cukup untuk jaga kesehatan dan kekuatan tubuh 💚")
        elif 60 < olahraga <= 90:
            print("🔥 Hebat! Kamu aktif banget, tapi jangan lupa istirahat cukup juga yaaa!")
        else:
            print("⚠ Jangan olahraga terlalu lama (>90 menit), nanti tubuh malah kelelahan 😔")

    print("\nTerima kasih udah ngecek hari ini🫰🏻 Semoga harimu tetap menyenangkan!")