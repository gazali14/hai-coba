# Numpy merupakan singkatan Numerical Python yang digunakan dalam memproses array
# Matplotlib digunakan untuk memvisualisasikan data kordinat menjadi garis
import numpy as np
import matplotlib.pyplot as plt

# Menginisialisasikan kordinat (x1,y1) dan kordinat (x2,y2)
x1 = int(input('Masukan x1  : '))
y1 = int(input('Masukan y1  : '))
x2 = int(input('Masukan x2  : '))
y2 = int(input('Masukan y2  : '))
print('------------------------------------------------')

# N adalah banyaknya iterasi yang dilakukan apabila x1 != x2 atau y1 != y2
nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

# titik awal x dan y
x = x1
y = y1

i = 1

# membuat pengkondisian dengan beberapa syarat seperti :

# ---> Jika x1 sama dengan x2 (garis vertikal), maka :
#       a. y = y + 1 dan x tetap
#       b. gambar titik kordinat (x,y)
#       c. tampilkan grafik (selesai)

# ---> Jika y1 sama dengan y2 (garis horizontal), maka :
#       a. x = x + 1 dan y tetap
#       b. gambar titik kordinat (x,y)
#       c. tampilkan grafik (selesai)

# ---> Jika 2 kondisi di atas salah, maka :
#       a. hitung kemiringan garis dengan m = (y2 - y1) / (x2 - x1) 
#       b. iterasi diulang sebanyak N
#       c. y = m ( x - x1 ) + y1
#       d. lakukan pembulatan pada y
#       e. gambar titik (x, y(pembulatan))
#       f. x = x + 1

if x1 == x2:
    titikX = []
    titikY = []
    while i < y2:
        if y1 == y2:
            print('Titik yang di lewati yaitu (',x,',',y,')' )
            titikX.append(x)
            titikY.append(y)
        else:
            print('Titik yang di lewati yaitu (',x,',',y,')')
            titikX.append(x)
            titikY.append(y+i)
        i+=1
    plt.plot(titikX,titikY)
    plt.scatter(titikX,titikY)
    plt.grid()
    plt.show()
    

elif y1 == y2:
    titikX = []
    titikY = []
    while i < y2:
        if x1 == x2:
            print('Titik yang di lewati yaitu (',x,',',y,')')
            titikX.append(x)
            titikY.append(y)
        else:
            print('Titik yang di lewati yaitu (',x,',',y,')')
            titikX.append(x+i)
            titikY.append(y)
        i+=1
    plt.plot(titikX,titikY)
    plt.scatter(titikX,titikY)
    plt.grid()
    plt.show()
else:
    titikX = []
    titikY = []
    while i <= N:
        m = nilaiY / nilaiX
        rumusY = m * (x - x1) + y1
        kordinatY = round(rumusY)
        x+=1
        print('Titik yang di lewati yaitu (',x-1,',',kordinatY,')')
        titikX.append(x-1)
        titikY.append(kordinatY)
        i+=1

# apppend digunakan untuk menambah item ke dalam array atau list
# plt.plot digunakan agar mathplotlib membuat titik pertemuan kordinat x,y
# plt.scatter digunakan untuk memplot titik yang dilalui garis
# plt.grid digunakan untuk menggambar grid
# plt.show digunakan agar mathplotlib menampilkan titik titik kordinat dari garis garis yang di lalui
    plt.plot(titikX,titikY)
    plt.scatter(titikX,titikY)
    plt.grid()
    plt.show()

#contoh ubah lagi nah