#project UAS Algoritma Pemograman
import os
if __name__ == "__main__":
    sistem_operasi = os.name
    
while(True):
    match sistem_operasi:
        case "nt": os.system("cls")  

    print(50*'-')
    print("SELAMAT DATANG DI SIPCAR RENTAL")
    print("ISI DATA DIRI ANDA TERLEBIH DAHULU")
    print(50*'-')
    nama=input(f"\nNama      :")
    umur=int(input("Umur      :"))
    dom=input(f"Domisili  :")
    if umur <=17 :
            print ("\nANDA BELOM CUKUP UMUR UNTUK MEMESAN!!")
            print ("SILAHKAN ULANGI KEMBALI MENGGUNAKAN DATA DIRI WALI ANDA ^_^")
            m=input("\n ENTER TO RELOAD")
    else :
        umur >17
        break

pake_1=(f"Paket 1 : (Mobil Avanza, Tahun 2015) Rp.500.000/hari")
pake_2=(f"Paket 2 : (Mobil Innova, Tahun 2019) Rp.700.000/hari")
pake_3=(f"Paket 3 : (Mobil Pajero, Tahun 2020) Rp.1.000.000/hari")
pake_4=(f"Paket 4 : (Mobil Alphard, Tahun 2021) Rp.1.100.000/hari")
pake_5=(f"Paket 5 : (Mobil Xpander, Tahun 2023) Rp.850.000/hari\n")

if __name__ == "__main__":
    sistem_operasi = os.name
    
    while(True):
        match sistem_operasi:
            case "nt": os.system("cls")
        
        print(50*'-')
        print("SELAMAT DATANG DI SIPCAR RENTAL")
        print("DI BAWAH ADALAH MENU-MENU UNTUK MELAKUKAN BOOKING")
        print(50*'-')   

        print(pake_1)
        print(pake_2)
        print(pake_3)
        print(pake_4)
        print(pake_5)



        paket = input("TENTUKAN PILIHAN ANDA... :") 
        if paket =="1"or paket =="2" or paket =="3" or paket =="4" or paket =="5": 
            break      
print("\n====================================================\n")
match paket:
    case "1": print(pake_1)
    case "2": print(pake_2)
    case "3": print(pake_3)
    case "4": print(pake_4)
    case "5": print(pake_5)

print("\n====================================================n")
hari=int(input("Berapa hari anda akan menyewa?  : "))
is_done = input("Tanggal anda akan mengambil mobilnya?(DD/MM)  :")



if(paket=='1'): 
    tpaket=(f"Avanza",2015,500000)
elif(paket=='2'):
    tpaket=(f"Innova",2019,700000)
elif(paket=='3'):
    tpaket=(f"Pajero",2020,1000000)
elif(paket=='4'):
    tpaket=(f"Alphard",2021,1100000)
elif(paket=='5'):
    tpaket=(f"Xpander",2023,850000)
else :
    tpaket=(f"")

if dom=="BATANG" or dom=="batang" or dom=="Batang" or dom=="btg" or dom=="BTG":
    dicount=(int(100000))
else :
    dicount=(int(0))

pay=(tpaket[2])*hari
if hari>=5:
    dch=(int(pay*0.1))
else :
    dch=(int(0))
tth=pay-dch-dicount


rpz=f"RP. {dch:,},00"
rphm=f"RP. {(tpaket[2]):,}.00"
rpds=f"RP. {dicount:,}.00"
rppay=f"RP. {tth:,}.00"

match sistem_operasi:
    case "nt": os.system("cls")

print("\n------------------------------------")
print("     SIPCAR RENTAL MOBIL TERBAIK")
print("             INVOICE ANDA")
print("------------------------------------\n")
print("")
print("Nama Penyewa         :",nama)
print("Domsili Penyewa      :",dom)
print("Merek Mobil          : %s"%(tpaket[0]))
print("Tahun Produksi Mobil : %d"%(tpaket[1]))
print("Harga Sewa perHari   :",rphm)
print("Tanggal Membawa Mobil:",is_done)
print("Jumlah hari sewa     :",hari)
print("Discount             :",rpds)
print("Discount Hari>5      :",rpz)
print("Total Harga          :",rppay)
print("")
print("\n------------------------------------")
print("     SIMPAN INVOICE ANDA LALU\n     KIRIM MELALUI WHATSAPP KAMI")
print("------------------------------------\n")
next_=input("TEKAN ENTER UNTUK KE MENU PEMBAYARAN...")
match sistem_operasi:
    case "nt": os.system("cls")

with open("database.txt", 'r', ) as file:
    pmbyr=file.read()

print(pmbyr)
kl=input("TERIMAKASIH SUDAH MELAKUKAN BOOKING ^_^")

