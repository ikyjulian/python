import time

a = int (input("asukaan jumlah siswa"))

for i in range(a):
    nama =("masukan nama siswa / siswi")
    tugas1 = float (input("maskan nilai tugas ke 1 anda: "))
    tugas2 = float (input("maskan nilai tugas ke 1 anda: "))
    tugas3 = float (input("maskan nilai tugas ke 1 anda:"))

    b = 3

    all = tugas1 + tugas2 + tugas3

    avv = all / b

    if avv >=70:
        print("selamat anda lulus")

    elif avv > 50 and avv < 69:
        print("anda harus perbaiki")

    elif avv <= 50:
        print("anda tidak lulus")

    else:
            print("anda tidak lulus")