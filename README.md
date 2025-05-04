# Tsui-No-Stella-IDN

<p align='center'>
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjepTmsHW8na4qiuprDH1HVp2wZOYdpPisbe4RSDgNqimAdOOslkDE9UymVBRZZwJarnZKsj-qx17D5FML9P27jW_CzOl9r8EUsG-QuCiBxeEaJHXF2j0RlYpfRGMBymcjDeFnMIhwNI9kqWdVhaSHZ9nBOwvM0pIYG4v3dnvVgZJ5j2plxkZa2xcc_RpE/s1350/tsn2.jpg"

<details open> 
  <summary><h2>Information</h2></summary>

- Judul (JP) : Tsui No Stella
- Judul (EN) : Stella of The End
- FanTL (ID) : Zero Novel Team
- Developer  : Key
- Released   : 2022-09-30
- Rating     : All Age
- Engine     : Artemis Engine
- VNDB       : v29443 [VNDB](https://vndb.org/v29443)

<details open> 
  <summary><h2>Isi Patch</h2></summary>

  - Movie + Subtitle 
  - Translated Script
  - Translated UI(Config, Image dalam story, Extra)

NOTE PENTING : Untuk yang sudah pernah memainankan Tsui No Stella dari Ryuugames maupun dari Steam diharapkan untuk membackup Savedata itu sebelum instalasi Patch

[Unduh Patch](https://github.com/Walkedharmony/Tsui-No-Stella-IDN/releases/tag/1.0)

<details open> 
  <summary><h2>Cara Instalasi Patch PC</h2></summary>

  - Sebelum instalasi perlu di ingat bahwa patch ini untuk engine Artemis(Steam Ver) saja 
  - Didalam patch Bahasa Indonesia terdapat 3 file dan folder(File patchnya.pfs.001, Folder Script dan Movie )
  - Drag And Drop isi dari rar itu dan taruh di direktori gamenya
    <p align='center'><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9deTOJtgn3ANR-kgurIdPbdj9a0QPew37Vyp5YMI_K8zE5aNjSI2GHmeHjbTOOgi3-_wc5RaorbrcGUcG0c5UTIQ6B5GAnAzRDSwOth4jci1uTis0hiCGU3crFIgt_6tSfbukbsLTy3Wdzi3qPzdsf5RGXvz-LSMFK-F9o-1VmnES6wmSGlqrAa3vACY/s827/Screenshot%202025-05-02%20184322.png"
  - Setelah selesai sesuai di gambar maka patch telah terpasang dan tinggal dimainkan

<details open> 
  <summary><h2>Artroid+ Version</h2></summary>

  - Jika sudah mempunyai base gamenya di PC entah dari ryuu/steam ver bisa di transfer ke android dan rename nama Archivesnya dari `Stella_of_The_End.pfs` ke `root.pfs`
  - Lakukan hal yang sama pada `Stella_of_The_End.pfs.000` menjadi `root.pfs.000`
  - Jika sudah selesai maka kalian bisa unduh [Patchnya](https://drive.google.com/file/d/1O1RdMX9QBEVEL7kVCL-0Zi6BC2U1Zr4T/view)
  - Dibawah ini adalah base game dari PC yang di transfer ke android
    <p align='center'><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9sXevT20ZVst9LZoMya4K3CL9oR3HfSwrKqniBM0i79H_680aIvsOgtBn_bscMYyiJTQ7rkWs3F1uFV6LFKc3wAxIBjWTP8KptXmtw14xBfnjMGYU33OY7VBBPLg45wGKURIpTuMDCfLsOLs96UcrNoVDGALXBu4QYyINyyzo_ymiwEFEhQPyGRoEej4/s823/Screenshot%202025-05-04%20174247.png" 
 - Dan di bawah ini adalah hasil akhir dari rename + patchnya
   <p align='center'><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgy_qAJZ8kGPf9rkSR0NDoAeqwNJ13cQRD-18btPkUmDWrcuodCWUeATkiKUOb5j3WO8utpWcVW0QazfmoTiF9IpEgnCMigcWUxM2DYfFDBS3V8yY-O5EHu2IF92NQ345Pe2SWC5c_uop2axgI3qKTS0djn37DTvnl3gFi48IIb520A3K0CyAQpSizf73Y/s775/Screenshot%202025-05-04%20174634.png" 

 Hasil Akhir untuk Artroid+ yang dibutuhkan : 

 
- Movie <-- Hanya ada 2 Movie yaitu Opening dan Ending
- Script <-- Inisiasi Opening
- System <-- Isi Tabel untuk Android 
- System.ini <-- System Config untuk Android
- root.pfs <-- Base Game 1 
- root.pfs.000 <-- Base Game 2
- root.pfs.001 <-- Patchnya Bahasa Indonesia

All Done 
- 
   <p align='center'><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgl6x7J4WiFvzXEJTuy8sv1Th7VpymrTOC8Q_udU3HvQG4ytZIXunsPq1c4DarM0yonp_kCKDsYBr2XGcnlGBvyJeY68NNf641YgjaPYC95gEN_CsmJf-BchA-1em42qk7SM72u_198B4TEEvHQHdeOBuabGP1EorQ6BkRcqK0phyXJOi39PWwDwdO3UNU/s1627/Screenshot%202025-05-03%20090008.png" 

<details open> 
  <summary><h2>Tools</h2></summary>

  - Parser : Untuk memparser bagian properti bahasa yang di pilih ke txt
  - Repacker : Untuk merepack txt ke ast kembali berdasarkan jumlah baris dan masih terjadi masalah dalam hasil repacker yaitu
               hasil simbol petik "" yang berlebih jadi diharapkan untuk di hapus dulu
  - GeneratePackFile2.exe : Untuk membuat patch untuk Artemis Engine
