def cek_mood():
    pertanyaan = [
        "1. Bagaimana suasana hatimu secara keseluruhan saat ini?",
        "2. Seberapa tenang dan nyaman perasaanmu saat ini?",
        "3. Seberapa stabil emosimu setelah melalui hari ini?",
        "4. Bagaimana tingkat stres atau ketegangan yang kamu rasakan saat ini?",
        "5. Seberapa puas kamu dengan hari yang kamu jalani hari ini?"
    ]
    
    daftar_opsi = [
        "   1. Sangat buruk",
        "   2. Buruk",
        "   3. Biasa saja",
        "   4. Baik",
        "   5. Sangat baik"
    ]
    
    jawaban = [] 
    print("=== How Are You Today? ===")
    print("Selamat Datang Diprogram cek suasana hati Anda hari ini😇🤩")
    print("Jawab setiap pertanyaan dengan daftar opsi (1-5)")
    print("1. Sangat buruk")
    print("2. Buruk")
    print("3. Biasa saja")
    print("4. Baik")
    print("5. Sangat baik\n")

    for i in pertanyaan:
        print(i)
        for x in daftar_opsi:
            print(x)
        while True:
            try:
                opsi = int(input("Masukkan opsi (1-5) : "))
                if opsi >= 1 and opsi <= 5:
                    jawaban.append(opsi)
                    break
                else:
                    print("Input hanya boleh memasukkan angka 1-5. Silahkan masukkan angka 1-5")
            except ValueError:
                    print("Input tidak valid. Silahkan masukkan angka 1-5")  

        print()
    
    total = 0 
    jumlah = 0

    for skor_mood in jawaban: 
        total += skor_mood
        jumlah += 1

    rata_rata = total / jumlah 

    print("=== Hasil Evaluasi Mood Anda Hari ini ===\n")
    print(f"Rata-rata mood kamu: {rata_rata:.2f}\n")
    if rata_rata <= 2:
        print(f"Ya:( Suasana hatimu sedang kurang baik hari ini😔. Gapapa kok, istirahat dulu ya😇")
    elif rata_rata <= 3:
        print(f"Hmzz.. suasana hatimu berada ditengah-tengah🙂. Tapi tetap tenang yaa, jangan sampe kamu down😉")
    else:
        print(f"Alhamdulillah YEYY suasana hatimu cukup baik hari ini🤩✨. Semoga energi positifnya berlanjut yaaa🌞")