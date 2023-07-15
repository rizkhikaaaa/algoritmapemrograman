#setting variable
nim  = input("masukkan nim")
name  = input("masukkan nama lengkap")
kls  = input("masukkan kelas")
prd  = input("masukkan nama prodi")

#setting variable nilai
ind  = int(input("Nilai Bahasa indonesia  :"))
ing  = int(input("Nilai Bahasa Inggris    :"))
pdsr     = int(input("Nilai Pemrograman Dasar :  "))
mtk    = int(input("Nilai Matematika        :  "))
kal1   = int(input("Nilai Kalkulus          :   "))


if(ind > 0 and ind <=60):
    gind= ("C")
elif(ind>60 and ind <=75) :
    gind = ("B")
elif(ind>75 and ind <=85) :
    gind= ("AB")
elif(ind >85 and ind<=100) :
    gind= ("A")
else: 
    gind=("Grade Anda Tidak ditemukan! ")
    
if(ing> 0 and ing <=60):
    gind2= ("C")
elif(ing>60 and ing<=75) :
    gind2 = ("B")
elif(ing>75 and ing<=85) :
    gind2= ("AB")
elif(ing>85 and ing<=100) :
    gind2= ("A")
else: 
    gind2=("Grade Anda Tidak ditemukan! ")
  
if(pdsr> 0 and pdsr<=60):
    gind3= ("C")
elif(pdsr>60 and pdsr<=75) :
    gind3 = ("B")
elif(pdsr>75 and pdsr<=85) :
    gind3= ("AB")
elif(pdsr>85 and pdsr<=100) :
    gind3= ("A")
else: 
    gind3=("Grade Anda Tidak ditemukan! ")
   
if(mtk > 0 and mtk <=60):
   gind4 = ("C")
elif(mtk>60 and mtk <=75) :
    gind4=("B")
elif(mtk >75 and mtk<=85) :
    gind4= ("AB")
elif(mtk>85 and mtk<=100) :
    gind4= ("A")
else: 
    gind4=("Grade Anda Tidak ditemukan! ")
   
if(kal1> 0 and kal1 <=60):
    gind5= ("C")
elif(kal1>60 and kal1<=75) :
    gind5= ("B")
elif(kal1>75 and kal1<=85) :
    gind5= ("AB")
elif(kal1>85 and kal1<=100) :
    gind5= ("A")
else: 
    gind5=("Grade Anda Tidak ditemukan! ")
   
   
#perhitungan
rata = (ind+ing+pdsr+mtk+kal1)/5

if(rata >0 and rata <=60) :
    grade_rata = ("C")
elif(rata >60 and rata <=75) :
    grade_rata = ("B")
elif(rata >75 and rata <=85) :
    grade_rata = ("AB")
elif(rata >85 and rata <=100) :
    grade_rata = ("A")
else: 
    grade_rata =("Grade Anda Tidak ditemukan! ")
   
#menampilkan
print("----------------------")
print("    kartu hasil studi     ")
print("----------------------")
print ("Nim           :",nim)
print ("nama lengkap  :",name)
print ("kelas         :",kls)
print ("program study :",pdsr)
print ("----------------------")
print ("No  Nama Makul   Nilai   Grade  ")
print ("----------------------")
print ("1.  bahasa Indonesia  ",ind,gind ), 
print ("2.  bahasa Inggris    ",ing,gind2 )
print ("3.  Pemrograman Dasar ",pdsr, gind3)
print ("4.  matematika        ",mtk, gind4)
print ("5.  Kalkulus 1        ",kal1, gind5 )
print ("----------------------")
print ("Rata-Rata             ",rata," ",grade_rata)
print ("----------------------")
