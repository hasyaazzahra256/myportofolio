Nama : Hasya Azzahra Rangkuti
NPM : 2506617512
Kelas : PBP A
PBP aku harus lulus!

### Log Progres Pengembangan (Weekly Progress)
* **Minggu 1 (Setup & Base Structure)**: Inisialisasi proyek Django, konfigurasi `settings.py`, pengaturan static files (`STATIC_URL` & `STATICFILES_DIRS`), serta pembuatan layout awal HTML.
* **Minggu 2 (Styling & Component Refinement)**: Implementasi CSS Grid & Flexbox, perancangan kartu pengalaman/keahlian yang konsisten, penyesuaian penanggalan kronologis real-time, perbaikan bug layout pada mobile viewport, serta dokumentasi penuh README.md.

### Tugas 1

1. Ya, saya pakai tag semantik HTML5 kayak <header>, <nav>, <main>, <section>, <article>, dan <footer>. Elemen-elemen ini membantu banget buat ngerapiin struktur kode supaya nggak numpuk tag <div> doang (div soup). Struktur web jadi lebih jelas bagian-bagiannya, misalnya <section> buat ngebagi modul (Profile, Skills, Experience, Education) dan <article> khusus buat kartu-kartu pengalaman. Selain bikin kodenya enak dibaca, ini juga membantu screen reader memahami isi web dan bikin struktur SEO-nya lebih rapi.

2. Tantangan paling berasa waktu atur CSS responsif itu pas nyesuaiin bagian Hero dan susunan kartu pengalaman biar nggak kelihatan mepet atau bikin scroll samping di HP. Waktu di layar laptop/desktop, bagian Hero aku buat 2 kolom (teks di kiri, foto di kanan). Tapi pas dibuka di layar HP (max-width: 600px), tata letaknya aku ubah jadi 1 kolom lurus ke bawah dengan urutan: Nama/NPM -> Foto Profil -> Bio & Kontak. Buat kartu-kartu pengalaman, saya  pakai grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)) supaya begitu layarnya mengecil, kartunya otomatis numpuk ke bawah secara rapi tanpa kepotong.

3. Keterbatasan paling berasa dari static web murni adalah kalau ada pembaruan data (misalnya mau nambah pengalaman atau skills baru), saya harus edit kodenya secara manual di HTML. Ini agak kurang praktis dan lumayan rawan typo. Selain itu, web statis belum bisa nampung masukan dari pengunjung secara langsung. Buat pengembangan berikutnya, saya ingin integrasiin Django ORM / Database biar data pengalaman bisa di edit lewat Django Admin, sama nambahin fitur Filter / Pencarian pakai JavaScript biar pengunjung bisa milih pengalaman berdasarkan kategori tertentu.

### Dokumentasi & AI Disclosure
Proyek ini dikembangkan dengan memanfaatkan AI (Gemini) sebagai pair-programmer, asisten code review, dan alat debugging.

### Tools & Log Prompting
Tool Utama: Gemini 2.5 Flash / Pro.
Log Prompting Ringkas:
1. "Bagaimana cara menyusun CSS Grid responsif untuk hero section dengan 2 kolom di desktop dan 1 kolom di mobile?"
2. "Bantu periksa sintaks HTML ini, kenapa kotak kartu pada pengalaman tertentu tidak muncul border putihnya?"

### Keterbatasan AI dan perbaikan manual yang saya lakukan

meski AI bantu banget buat analisis kode  dengan cepat, tetep ada beberapa hal yang keliru dan harus saya perbaiki sendiri secara manual:

1. **Typo pada Class HTML**:
   * Masalah: Ada satu kartu pengalaman yang kotaknya kelihatan aneh/transparan karena typo penulisan class, yaitu `class="aproject-card"`.
   * Perbaikan: Saya cek lewat *Inspect Element* di browser, terus saya benerin nama class-nya jadi `project-card` biar kodenya balik normal. Saya juga nambahin aturan CSS media query biar tampilan kartunya nggak mendem atau menyempit pas dibuka di HP.

2. **Deskripsi Skills yang Terlalu Berlebihan**:
   * Masalah: AI sempet ngasih saran istilah skill yang ketinggian dan kurang cocok, kayak *User Research* atau *Prototyping Complex Architecture*.
   * Perbaikan: Saya ubah manual biar lebih jujur dan sesuai sama kemampuanku sekarang, yaitu fokus ke **UI Design & Visuals** (*Figma, Web Layout Design, Wireframing, Visual Assets*).

3. **Pemeriksaan Tanggal Pengalaman Organisasi**:
   * Perbaikan: Semua bulan dan tahun di 7 kartu pengalaman organisasi (kayak COMPFEST 18, RISTEK, BEM Fasilkom UI, WCE 2026, BETIS, Open House, dan OIM UI) aku cek dan sesuaikan manual satu per satu biar jadwalnya beneran pas.

### Tugas 2

1. **Alur Permintaan Pengguna (Request-Response Cycle):**
   - User mengetik atau mengklik link `/projects/` di browser.
   - Permintaan masuk dulu ke `portofolio/urls.py`, lalu diteruskan ke `main/urls.py`.
   - Di `main/urls.py`, path `'projects/'` dicocokkan dan memanggil fungsi `show_project` yang ada di `views.py`.
   - `views.py` minta data ke model `Project` pakai query `Project.objects.all()`.
   - Model ngambil data dari database dan mengembalikannya ke `views.py`.
   - `views.py` masukin data itu ke dalam `context`, lalu ngirim ke template `project.html`.
   - `project.html` merender datanya pakai Django Template Language (DTL) jadi tampilan HTML akhir yang dilihat di browser.

2. **Alasan Data Disimpan di Model:**
   - **Separation of Concerns:** Memisahkan data dan tampilan biar kode nggak berantakan.
   - **Gampang di-maintain:** Kalau mau nambah atau ubah data proyek, tinggal olah dari database/admin tanpa perlu bongkar-bongkar file HTML lagi.
   - **Scalable:** Lebih siap kalau nanti mau dibikin fitur form input, search, atau filter data.

3. **Perbedaan `makemigrations` dan `migrate`:**
   - **`makemigrations`**: Cuma menyiapkan atau membuat blueprint (berkas migrasi) berdasarkan perubahan di `models.py`. Database asli belum berubah di tahap ini.
   - **`migrate`**: Eksekusi blueprint tersebut ke database biar tabelnya beneran dibuat atau diperbarui.
   - **Contoh:** Pas kita nambahin model `Project` di `models.py`, kita jalanin `python manage.py makemigrations` buat ngebikin file `0002_project.py`, baru abis itu jalanin `python manage.py migrate` buat bikin tabel `main_project` di database.