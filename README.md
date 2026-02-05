Nuryadi Eka Haibah Za'im Hakim   
Absen : 26  
Kelas 11 RPL 5  

# Hasil Laporan Praktikum OOP

**1. Tugas Analisis 1 : **
Mengubah hero1.hp menjadi 500

code :  
class Hero:
 # Constructor: Dijalankan saat Hero baru dibuat
 def __init__(self, name, hp, attack_power):
  self.name = name # Nama Hero
  self.hp = hp # Nyawa (Health Point)
  self.attack_power = attack_power # Kekuatan Serangan
 # Method untuk menampilkan info hero
 def info(self):
  print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")
# -- Main Program --
# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 500, 15)
hero2 = Hero("Zilong", 120, 20)
# Memanggil Method
hero1.info()
hero2.info()

print(hero1.hp)

**1. Tugas Analisis 2 : **


**1. Tugas Analisis 3 : **


**1. Tugas Analisis 4 : **


**1. Tugas Analisis 5 : **


**1. Tugas Analisis 6 : **
