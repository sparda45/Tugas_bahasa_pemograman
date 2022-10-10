import socket

import sys

class utama():
 def __init__(self) :

  print("masukan pilihan")
print("1. server")
print("2. client")
print("3. keluar")

pilihan = input("masukan pilihan anda :")

if pilihan == "1":
    lokasi = socket.gethostbyname("192.168.1.137")
    s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    s.bind ( (lokasi, 2121))
    s.listen (5)
    print("server aktif")
    client, alamat = s.accept ()
    print ("Menerima koneksi dari : ", alamat)
    while True :
        data = client.recv(1024).decode()
        if not data:
            break;
        print("pesan masuk :", str(data))
        data = input(">")
        client.send(data.encode())
        
elif pilihan== "2":
    alamatserver = input("masukan alamat server")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect ((alamatserver, 2121))
    
    pesan = input(">")
    
    while pesan !="bye" :
          s.send(pesan.encode())
          data = s.recv(1024).decode()
          print("server :",data)
          pesan = input(">")
else:
    quit()
    
if __name__ == " main":
    utama()
    sys.exit()

