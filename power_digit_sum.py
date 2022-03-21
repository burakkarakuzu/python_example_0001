number0=0
#Sayı girişi
number=input("Number of enter:")
#Sayının kuvvetini al
#Sayıyı Stringe çevirerek for döngüsü aç
for number_str in str(number):
    if int(number_str) !=0:
        number0 +=int(number_str)
#Bu sayıyı ekrana yazdır
print(number," sayısının rakamları toplamı:",int(number0),"\n")