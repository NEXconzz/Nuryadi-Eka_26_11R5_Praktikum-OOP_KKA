Nuryadi Eka Haibah Za'im Hakim   
Absen : 26  
Kelas 11 RPL 5  

# Hasil Laporan Praktikum OOP

**1. Tugas Analisis 1 :**   

code :  

<img width="1835" height="429" alt="Screenshot 2026-02-05 141817" src="https://github.com/user-attachments/assets/d4d8b221-ed63-48a2-af37-ae64eb2c979c" />  

jawab :  
1. 500 print(hero1.hp) Yang muncul 500, tapi itu bukan HP asli. Soalnya HP asli disimpan di __hp.

  **2. Tugas Analisis 2 :**  

  code :  

  <img width="1843" height="719" alt="Screenshot 2026-02-05 142633" src="https://github.com/user-attachments/assets/b152639f-00f1-4b53-962c-493e665b0797" />  

jawab :
1. karena yang dibutuhkan bukan hanya nama lawan, tetapi juga data lain nya, seperti hp dan method lawan. jika hanya string, maka data lain itu tidak dapat dibaca dan tidak dapat diserang.  

**3. Tugas Analisis 3 :**  

code :  

<img width="1808" height="798" alt="Screenshot 2026-02-05 180653" src="https://github.com/user-attachments/assets/d4919add-c8a4-46b4-b1e8-f1fe51cc01f0" />  
<img width="1764" height="746" alt="Screenshot 2026-02-05 180710" src="https://github.com/user-attachments/assets/04e4572c-4535-49e4-b564-b3fec8c80412" />  

jawab :  

1. kenapa terjadi error ketika menghaous super()._init_(), karena constructor hero tidak bisa dijalankan sehingga membuat data milik hero tidak ikut dibuat.  
2. Fungsi super() adalah untuk memanggil constructor class induk agar data bisa dimasukan ke class anak.  

**4. Tugas Analisis 4 :**  

code:  

<img width="1773" height="714" alt="Screenshot 2026-02-05 183404" src="https://github.com/user-attachments/assets/809f9fb5-429e-4057-af71-1f9897a7b402" />  

jawab :  

1. Akses Paksa HP print(hero1._Hero__hp) HP tetap muncul. Karena Python cuma “nyamarin” nama, bukan ngunci total.  
2. Setter Tanpa Aturan Kalau set_hp nggak pakai pengecekan, lalu: hero1.set_hp(-100) HP jadi -100. HP nggak mungkin minus.  

**5 Tugas Analisis 5 :**  

code :  

<img width="1757" height="755" alt="Screenshot 2026-02-05 190614" src="https://github.com/user-attachments/assets/62c2ee46-b92f-4cce-a7a9-21895ffbe0f0" />  

jawab :  
1. jika method serang dihapus, akan menghasilkan error "TypeError: Can't instantiate abstract class Hero without an implementation for abstract method 'serang' " yang berarti hero tersebut tidak memenuhi aturan dari Gameunit.
2. Gameunit tidak dapat dijadikan object, karena Gameunit memiliki fungsi sebagai kerangka atau aturan, bukan hero.  

**6. Tugas Analisis 6 :**  

code :  

<img width="693" height="743" alt="Screenshot 2026-02-05 193530" src="https://github.com/user-attachments/assets/cc9ad8c7-b2c4-4442-8f97-091fc0e519ad" />  

jawab :  

1. Program tetap berjalan lancar tanpa mengubah loop walaupun menambah class healer.
2. ketika method serang pada archer digantikan dengan tembak_panah, program tetap berjalam, tetapi pada class acher tidak akan mengeluarkan keterangan seperti class lainya, melainkan akan muncul "Hero menyerang dengan tangan kosong." karena sistem mencari method serang.
