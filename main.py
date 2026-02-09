import time
import random

def print_dramatis(teks):
    """Menampilkan teks dengan jeda 0.5 detik untuk efek dramatis"""
    print(teks)
    time.sleep(0.5)

def tampilkan_pedang():
    """Menampilkan ASCII art pedang ketika pemain menang"""
    pedang = """
    ⚔️  KEMENANGAN ANDA!  ⚔️
    
        ╱╲
       ╱  ╲
      ╱    ╲
     ╱  ║   ╲
    ╱   ║    ╲
   ╱    ║     ╲
  ╱     ║      ╲
 ╱      ║       ╲
╱───────║────────╲
        ║
        ║
       ╱ ╲
      ╱   ╲
    """
    print(pedang)

def tampilkan_tengkorak():
    """Menampilkan ASCII art tengkorak ketika pemain kalah"""
    tengkorak = """
    ☠️  ANDA TELAH KALAH  ☠️
    
      ██████╗ 
     ██╔════╝ 
     ██║  ███╗
     ██║   ██║
     ╚██████╔╝
      ╚═════╝ 
      
     █████████
    ███░░░░░███
   ██░░░░░░░░██
   ██░░░░░░░░██
    ███░░░░░███
     █████████
    """
    print(tengkorak)

def game_utama():
    print_dramatis("--- PROLOG: NARATOR MENGAMATI ---")
    nama = input("Siapa namamu? ")
    nyawa = 100
    skor = 0
    print_dramatis(f"\nSelamat datang, {nama}. Aku melihat jalurmu sebelum kau melangkah — cerita ini bergulir oleh pilihan yang kau buat.")
    print_dramatis(f"Status awal — nyawa: {nyawa}. Semesta mencatatnya.")
    time.sleep(1)

    # Main loop: 6 ronde total (babak awal + 5 babak lanjutan)
    total_ronde = 6
    for ronde in range(1, total_ronde + 1):
        nyawa, skor, lanjut = play_round(ronde, nama, nyawa, skor)
        if not lanjut or nyawa <= 0:
            break

    # Ending
    time.sleep(1)
    if nyawa > 0:
        tampilkan_pedang()
        print_dramatis(f"\n🎉 Selamat, {nama}! Anda menyelesaikan petualangan dengan nyawa {nyawa} dan skor {skor} ✅")
    else:
        tampilkan_tengkorak()
        print_dramatis(f"\n💀 Sayang sekali, {nama}... Petualangan Anda telah berakhir. Skor: {skor}")

    print_dramatis("\n--- TERIMA KASIH TELAH BERMAIN ---")


def play_round(ronde, nama, nyawa, skor):
    """Menjalankan satu ronde permainan. Mengembalikan (nyawa, skor, lanjut_bool)."""
    print_dramatis(f"\n--- Babak {ronde} ---")
    # Ronde 1: Persimpangan awal
    if ronde == 1:
        print_dramatis("Di persimpangan yang sunyi, sang narator menulis: pilihanmu akan mengubah nada cerita ini.")
        print_dramatis("Pilih jalurmu:\n1. Lembah Coding — ketenangan di antara baris\n2. Gunung Bug — gema error yang menganga\n3. Jalan Tengah — tipu daya yang menggoda")
        pilihan = input("Pilih jalur (1/2/3): ")
        if pilihan == "1":
            print_dramatis(f"\n{nama} melangkah ke Lembah Coding. Sang narator menulis bahwa baris-baris kode berbisik menenangkannya.")
            keberuntungan = random.randint(1, 100)
            if keberuntungan > 60:
                hadiah = random.randint(10, 25)
                skor += hadiah
                nyawa += 5
                print_dramatis(f"🍀 Entitas kecil tersenyum: kau menerima +{hadiah} skor dan +5 nyawa, narator mencatatnya dengan tenang.")
            elif keberuntungan > 20:
                skor += 5
                print_dramatis("✅ Kau lewat tanpa gangguan; sebuah snippet kecil terselip di sela-sela — +5 skor, catat narator.")
            else:
                damage = random.randint(8, 18)
                nyawa -= damage
                print_dramatis(f"⚠️ Sebuah kecacatan muncul; kau kehilangan -{damage} nyawa. Narator menghela napas.")
        elif pilihan == "2":
            print_dramatis(f"\n{nama} mendaki Gunung Bug. Di puncak, narator melihat awan peringatan menggulung.")
            keberuntungan = random.randint(1, 100)
            if keberuntungan > 75:
                bonus = random.randint(20,40)
                skor += bonus
                print_dramatis(f"🍀 Keberuntungan besar; cerita berbalik — kau menaklukkan rintangan dan mendapat +{bonus} skor, tertulis di manuskrip tak terlihat.")
            elif keberuntungan > 40:
                damage = random.randint(15, 30)
                nyawa -= damage
                print_dramatis(f"⚠️ Exception menyerang; narator mencatat luka: -{damage} nyawa")
            else:
                damage = random.randint(30, 55)
                nyawa -= damage
                print_dramatis(f"💥 Sebuah NullPointerException melanda keras; narator menulis tragedi: -{damage} nyawa")
        elif pilihan == "3":
            print_dramatis("Jalan Tengah — tindakan tergesa. Narator memperingatkan: jalan pintas memikat namun berbahaya.")
            chance = random.randint(1,100)
            if chance > 65:
                skor += 30
                print_dramatis("🚀 Shortcut sukses! Narator mencatat lonjakan: +30 skor")
            elif chance > 30:
                skor += 10
                nyawa -= 10
                print_dramatis("🛠️ Sukses dengan biaya; +10 skor, -10 nyawa — narator menuliskannya tanpa menghakimi.")
            else:
                damage = random.randint(20,40)
                nyawa -= damage
                print_dramatis(f"💣 Shortcut runtuh; babak ini kelam: -{damage} nyawa, catat narator.")
        else:
            damage = random.randint(10, 20)
            nyawa -= damage
            print_dramatis("❌ Pilihan tidak valid! Anda kehilangan waktu dan nyawa karena syntax error.")
            print_dramatis(f"-{damage} nyawa")

    # Ronde 2: Pasar permutation
    elif ronde == 2:
        print_dramatis("Di Pasar Permutasi, pedagang berbisik pada narator; tawaran terhampar seperti pilihan takdir:")
        print_dramatis("1. Ramuan Penyembuh — mengembalikan keadaan, jika kau memilihnya")
        print_dramatis("2. Kartu Keberuntungan — hadiahnya tertulis di balik tinta nasib")
        print_dramatis("3. Peta Rahasia — selembar peta yang mungkin menyingkap celah aman di babak-babak nanti")
        pilihan = input("Pilih item (1/2/3): ")
        if pilihan == "1":
            heal = random.randint(15, 25)
            nyawa += heal
            print_dramatis(f"✨ Kau menenggak ramuan; narator menulis bahwa tubuhmu pulih +{heal} nyawa.")
        elif pilihan == "2":
            chance = random.randint(1, 100)
            if chance > 60:
                bonus = random.randint(15,40)
                skor += bonus
                print_dramatis(f"🍀 Keberuntungan—narator menulisnya—memberi +{bonus} skor dari kartu.")
            else:
                damage = random.randint(10,30)
                nyawa -= damage
                print_dramatis(f"🕳️ Kartu itu berisi cela; kau kehilangan -{damage} nyawa, tercatat dalam naskah.")
        elif pilihan == "3":
            print_dramatis("🗺️ Peta rahasia — narator tersenyum — mengungkap jalan aman di babak-babak mendatang. +5 skor.")
            skor += 5
        else:
            print_dramatis("Pemilihan yang janggal — pedagogang tertawa membisik pada narator; peluang hilang tanpa bekas.")

    # Ronde 3: Labirin Algoritma
    elif ronde == 3:
        print_dramatis("Di Labirin Algoritma, narator melihat tiga jalan — masing-masing bersuara dengan alunan berbeda:")
        print_dramatis("1. Kiri — ke dalam perpustakaan kuno, di mana naskah tersenyum")
        print_dramatis("2. Kanan — gema loop tak berujung, namun skor bersembunyi di dalam")
        print_dramatis("3. Terowongan Rahasia — permata terpendam atau bencana, narator tidak yakin")
        pilihan = input("Pilih jalan (1/2/3): ").lower().strip()
        if pilihan == "1" or pilihan == "kiri":
            print_dramatis("Jalan kiri membawa Anda ke dalam perpustakaan; snippet berguna bersembunyi di rak tua. Narator mencatatnya dengan nyaman.")
            skor += 12
            nyawa += 5
        elif pilihan == "2" or pilihan == "kanan":
            damage = random.randint(10,25)
            nyawa -= damage
            skor += 15
            print_dramatis(f"Loop tak berujung menyerang; kau kehilangan -{damage} nyawa, namun skor melonjak +15. Ironi yang narator catat.")
        elif pilihan == "3":
            chance = random.randint(1,100)
            if chance > 65:
                bonus = random.randint(30,60)
                skor += bonus
                print_dramatis(f"🎁 Terowongan rahasia menyingkap harta karun; +{bonus} skor. Narator bersukacita.")
            else:
                damage = random.randint(20,40)
                nyawa -= damage
                print_dramatis(f"💥 Terowongan runtuh; narator menghela—keberuntungan berbelok: -{damage} nyawa")
        else:
            print_dramatis("Anda tersesat sejenak dan kehilangan waktu berharga.")

    # Ronde 4: Riddle dari NPC
    elif ronde == 4:
        print_dramatis("NPC kuno berdiri di persimpangan; narator mendengarnya berbisik teka-teki yang telah dimulai:")
        print_dramatis("1. Jawab teka-teki — risiko kegagalan")
        print_dramatis("2. Tawari bantuan — path hati nurani")
        print_dramatis("3. Lewati — mengabaikan kesempatan")
        pilihan = input("Pilih aksi (1/2/3): ").lower().strip()
        if pilihan == "1":
            jawaban = input("Jawaban Anda: ").lower().strip()
            if "jam" in jawaban or "waktu" in jawaban:
                print_dramatis("Benar! NPC tersenyum — narator mencatat berkah yang diberikan. +25 skor, +10 nyawa.")
                skor += 25
                nyawa += 10
            else:
                damage = random.randint(10,20)
                nyawa -= damage
                print_dramatis(f"Salah — NPC menggeleng, melangkah pergi dengan kecewa. Narator mencatat: -{damage} nyawa")
        elif pilihan == "2":
            print_dramatis("Kau memberi NPC sesuatu yang patut dihargai — informasi, kemurahan hati. Narator mencatatnya: +15 skor.")
            skor += 15
        elif pilihan == "3":
            print_dramatis("Kau berlalu begitu saja; narator menulis bahwa peluang entah muncul atau lenyap tanpa bekas.")
        else:
            print_dramatis("NPC bingung mendengarkan pilihan aneh; narator hanya terdiam.")

    # Ronde 5: Jembatan Depan API
    elif ronde == 5:
        print_dramatis("Jembatan API terbentang di depan, rapuh, bergetar dengan detak nadi data. Narator melihat tiga jalan:")
        print_dramatis("1. Lompat — cerita kilat, takdir gelisah")
        print_dramatis("2. Perbaiki — narasi lambat, aman tapi lelah")
        print_dramatis("3. Panggil bantuan — sumber daya untuk keselamatan")
        pilihan = input("Pilih aksi (1/2/3): ")
        if pilihan == "1":
            keberuntungan = random.randint(1,100)
            if keberuntungan > 55:
                skor += 25
                print_dramatis("Melompat! Narator melihat kau terbang melintasi jembatan dengan elegan — +25 skor.")
            else:
                damage = random.randint(15,35)
                nyawa -= damage
                print_dramatis(f"Melompat dan jatuh! Narator menuliskan kesedihan: -{damage} nyawa")
        elif pilihan == "2":
            print_dramatis("Perbaikan lambat dan teliti — cerita bertahan. Kelelahan menyentuh (-8 nyawa), namun jembatan kokoh (+5 skor).")
            nyawa -= 8
            skor += 5
        elif pilihan == "3":
            if skor >= 20:
                skor -= 20
                print_dramatis("Anda menyewa bantuan dan jembatan aman; -20 skor")
            else:
                damage = random.randint(10,25)
                nyawa -= damage
                print_dramatis(f"Tidak cukup skor untuk bantuan: -{damage} nyawa")
        else:
            print_dramatis("Waktu habis — jembatan runtuh sedikit di bawah kaki Anda.")
            nyawa -= 15

    # Ronde 6: Pertempuran Boss (akhir)
    elif ronde == 6:
        print_dramatis("Akhirnya, Anda menghadapi Sang Bug Besar — pertarungan menentukan nasib!")
        print_dramatis("1. Serangan logika (berisiko)  2. Defensive refactor (aman)  3. Gunakan item khusus jika ada")
        pilihan = input("Pilih strategi (1/2/3): ")
        if pilihan == "1":
            power = random.randint(30,60)
            sukses = random.randint(1,100)
            if sukses > 35:
                skor += power
                print_dramatis(f"Serangan berhasil! Anda memberi {power} damage ke boss (skor +{power})")
            else:
                damage = random.randint(20,40)
                nyawa -= damage
                print_dramatis(f"Serangan gagal dan Anda terluka: -{damage} nyawa")
        elif pilihan == "2":
            reduce = random.randint(15,30)
            nyawa -= max(0, reduce//2)
            skor += 10
            print_dramatis(f"Strategi defensif sukses: -{reduce//2} nyawa, +10 skor")
        elif pilihan == "3":
            if skor >= 30:
                skor -= 30
                print_dramatis("Anda menggunakan item khusus: serangan besar ke boss! +50 skor")
                skor += 50
            else:
                print_dramatis("Anda tidak punya item khusus yang cukup. Boss menyerang")
                damage = random.randint(20,35)
                nyawa -= damage
        else:
            damage = random.randint(25,45)
            nyawa -= damage
            print_dramatis(f"Strategi tidak valid! Boss memanfaatkan celah: -{damage} nyawa")

    # Tampilkan status setelah ronde
    print_dramatis(f"Status akhir Babak {ronde}: Nyawa={nyawa} ❤️ | Skor={skor}")
    # Jika nyawa habis, hentikan permainan
    if nyawa <= 0:
        return nyawa, skor, False
    # Lanjutkan ke ronde berikutnya
    return nyawa, skor, True

def main():
    """Loop utama untuk memungkinkan pemain bermain lagi"""
    main_lagi = True
    while main_lagi:
        game_utama()
        time.sleep(1)
        jawaban = input("\nMain lagi? (y/n): ").lower().strip()
        if jawaban == "y" or jawaban == "yes":
            print("\n" + "="*50 + "\n")
            main_lagi = True
        else:
            print_dramatis("\n👋 Sampai jumpa lagi, petualang! Terima kasih telah bermain!")
            main_lagi = False

if __name__ == "__main__":
    main()