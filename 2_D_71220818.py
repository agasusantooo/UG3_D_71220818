platnomor=input("Masukkan Plat Nomor :").lower().split(" ")


try:
    angkaplat=int(platnomor[1])
    if(angkaplat>0 and angkaplat<3001):
        print("Plat nomor diperuntukkan untuk mobil")
    elif(angkaplat>3000 and angkaplat<4001):
        print("Plat nomor diperuntukkan untuk motor")
    elif(angkaplat>4000 and angkaplat<5001):
        print("Plat nomor tersebut untuk angkutan umum")
except:
    print("Plat nomor tidak terindikasi, setelah kode daerah harus berupa nomor kendaraan")



