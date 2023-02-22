
nama=input("Masukkan Nama Lengkap Anda : ")
prodi=input("Masukkan Prodi Anda : ")
hurufnilai=input("Masukkan Nilai (dalam Huruf) yang Anda Dapat : ")
try:
    if(hurufnilai=="A"):
        print("Nilai anda adalah 4.0, tbl tbl serem bgt lohh")
    elif(hurufnilai == "A-"):
        print("Nilai anda adalah 3.75, kamu keren!") 
    elif(hurufnilai == "B+"):
        print("Nilai anda adalah 3.25, pertahankan!")
    elif(hurufnilai == "B"):
        print("Nilai anda adalah 3.0, lumayan bagus kok")
    elif(hurufnilai == "B-"):
        print("Nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif(hurufnilai == "C+"):
        print("Nilai anda adalah 2.25, lebih rajin lagi belajarnya")
    elif(hurufnilai == "C"):
        print("Nilai anda adalah 2.0, tugas kamu gapernah dikerjain?")
    elif(hurufnilai == "D"):
        print("Nilai anda adalah 1, apakah sudah ada pikiran untuk pindah jurusan?")
    elif(hurufnilai == "E"):
        print("Nilai anda adalah 0, niat kuliah nggak sih???")
    else:
        print("Inputan nilai yang anda masukkan tidak valid")
except:
    print("tes")