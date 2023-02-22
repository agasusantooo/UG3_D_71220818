awalderet=int(input("Masukkan awal deret :"))
akhirderet=int(input("Masukkan akhir deret :"))
hasilderet = [int(deret) for deret in range(awalderet, akhirderet) if deret % 6 != 0 and deret % 8 != 0]

print(" ".join(hasilderet))