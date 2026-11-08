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

### Tugas 3

1. Penggunaan `ModelForm` di Django itu bantu banget karena kita engga perlu lagi bikin tag `<input>` dan `<form>` secara manual satu-per-satu di berkas HTML. `ModelForm` otomatis membaca skema dari model Django yang kita buat (seperti tipe data, batasan karakter, hingga jenis field-nya) lalu bikin form-nya secara otomatis. Selain itu, `ModelForm` juga sudah dilengkapi validasi bawaan yang ketat dan proses penyimpanan data ke database yang praktis banget, cukup pakai `form.save()`. Mengenai `{% csrf_token %}`, tag ini wajib dimasukkan di dalam setiap form HTML agar aplikasi kita terlindungi dari serangan *Cross-Site Request Forgery* (CSRF). Token keamanan acak ini memastikan bahwa permintaan ubah/tambah data benar-benar berasal dari pengguna di situs web kita, bukan dari situs peretas luar.

2. JSON lebih banyak dipakai di pengembangan web modern daripada XML karena formatnya jauh lebih ringan dan ringkas tanpa tag pembuka/penutup yang panjang berulang. Selain itu, JSON adalah format *native* dalam JavaScript, sehingga browser dapat melakukan *parsing* data JSON dengan jauh lebih cepat dan hemat memori daripada memproses dokumen XML yang rungkut. JSON juga memiliki struktur *key-value pair* yang intuitif dan langsung cocok dengan tipe data modern seperti object, array, string, dan number.

3. Alur pengembalian data JSON dimulai saat client (seperti browser atau Postman) mengirimkan permintaan HTTP GET ke endpoint API (misalnya `/api/experiences/`). Fungsi view di Django menerima permintaan tersebut, mengambil data dari database menggunakan ORM (`Experience.objects.all()`), lalu memanggil fungsi `serializers.serialize('json', ...)` untuk mengonversi objek ORM Django tersebut menjadi teks berformat JSON. Terakhir, string JSON ini dikembalikan ke client lewat `HttpResponse` dengan `content_type="application/json"`. Proses *serialization* ini wajib dilakukan karena objek ORM Django adalah instance Python internal yang tidak bisa langsung dikirim via jaringan HTTP. *Serialization* bertindak sebagai penerjemah yang mengubah objek Python menjadi bentuk teks terstruktur yang dipahami secara universal oleh browser maupun aplikasi lain.

### Dokumentasi & AI Disclosure
Pada pengerjaan Tugas 3 ini, saya kembali menggunakan AI (Gemini) sebagai asisten pemograman, panduan refactoring kode, dan alat debugging.

### Tools & Log Prompting
Tool Utama: Gemini 2.5 Flash / Pro.
Log Prompting Ringkas:
1. "Bagaimana cara membuat fungsi view CRUD lengkap untuk model Experience di Django beserta endpoint JSON-nya?"
2. "Bantu sesuaikan tampilan tombol Edit dan Delete di experience.html agar menggunakan tema warna pink (#D86B88) dan konsisten dengan komponen kartu yang sudah ada."

### Keterbatasan AI dan perbaikan manual yang saya lakukan

Meski AI sangat membantu mempercepat penulisan logika views dan form, tetap ada beberapa hal yang keliru dan harus saya selaraskan secara manual:

1. **Penyesuaian Primary Key (`uuid` vs `int`) pada URLs**:
   * Masalah: AI sempat memberikan contoh path URL dengan konverter `<uuid:id>`, padahal primary key model pada database lokal saya menggunakan tipe integer standar bawaan Django (`<int:id>`).
   * Perbaikan: Saya memeriksa struktur model di database dan menyesuaikan kembali pola `urls.py` menjadi `<int:id>` agar tidak memicu error 404/500 saat tombol Edit atau Delete diklik.

2. **Penyelarasan Warna dan Class CSS Tombol**:
   * Masalah: Tombol "+ Add Experience", "Edit", dan "Delete" yang disarankan AI menggunakan warna merah standar Bootstrap (`#e53e3e`), yang membuat tampilannya tidak serasi dengan tema warna utama portofolio saya.
   * Perbaikan: Saya mengedit kode HTML secara manual untuk mengganti warna tombol menjadi warna pink (`#D86B88`) serta menyesuaikan padding dan *border-radius* agar tombol terlihat lebih estetis.

3. **Integritas Deserialisasi Data pada Views**:
   * Masalah: Saat deserialisasi JSON dilakukan di fungsi `show_experience`, field `id` tidak otomatis terbawa ke dalam *dictionary* yang di-pass ke template, sehingga link tombol `edit` dan `delete` sempat kehilangan referensi ID objek.
   * Perbaikan: Saya memperbaiki logika perulangan di `views.py` secara manual dengan menyisipkan atribut `exp_data['id'] = item['pk']` sebelum dikirimkan ke dalam context `experience.html`.


### Tugas 4

1. **Bagaimana implementasi *Role-Based Access Control* (RBAC) pada proyek ini?**  
   Implementasi RBAC dilakukan dengan memanfaatkan fitur bawaan Django `Group` dan atribut `is_superuser` pada model `User`:
   - **User Biasa (Visitor/Non-Editor)**: Hanya memiliki akses *read-only*. Mereka hanya bisa melihat daftar Experience dan Projects, serta melakukan aksi *starring* (toggle star) pada proyek.
   - **Editor (Grup 'Editor')**: Diberikan hak akses untuk membuat (`create`), mengubah (`edit`), dan menghapus (`delete`) data Experience maupun Projects.
   - **Superuser (Admin)**: Memiliki hak akses penuh (*full access*) terhadap seluruh sistem, baik melalui Django Admin maupun antarmuka aplikasi utama.

2. **Bagaimana cara memastikan hak akses keamanan tetap terjaga di level backend dan frontend?**  
   - **Level Backend (Views & Endpoint)**: Mengecek peran pengguna di setiap view yang melakukan manipulasi data (`create`, `edit`, `delete`) menggunakan fungsi penolong `is_editor(user)` dan `request.user.is_superuser`. Jika pengguna yang belum terautentikasi atau bukan anggota grup Editor/Superuser mencoba mengakses URL secara langsung, sistem akan memicu `PermissionDenied` (HTTP 403) atau mengarahkannya ke halaman login (`@login_required`).
   - **Level Frontend (Templates)**: Menggunakan logika pengkondisian Django Template (`{% if user.is_superuser or is_editor %}`) untuk menyembunyikan tombol-tombol sensitif seperti **+ Add**, **Edit**, dan **Delete**. Dengan begitu, pengguna biasa tidak akan melihat elemen antarmuka yang tidak menjadi hak aksesnya.

3. **Bagaimana cara menjaga keamanan data pada endpoint JSON dari kebocoran informasi sensitif?**  
   Pada fungsi `get_experiences_json` dan `get_projects_json` di `views.py`, pembatasan dilakukan secara eksplisit menggunakan parameter `fields` saat meng-serialize data ke JSON (misalnya `fields=('title', 'description', 'tech_stack', 'project_url', 'thumbnail')`). Dengan cara ini, relasi ke model `User` atau metadata internal yang berpotensi membocorkan data sensitif pengguna (seperti *password hash*, email rahasia, atau tanggal login) tidak ikut terekspos ke publik melalui endpoint JSON API.


### Dokumentasi & AI Disclosure (Tugas 4)
Proyek pada Tugas 4 ini dikembangkan dengan memanfaatkan AI (Gemini) sebagai pair-programmer, membantu memandu langkah-langkah konfigurasi grup Django Admin, merancang fungsi penolong RBAC, serta melakukan pembatasan serialization data.

### Tools & Log Prompting
- **Tool Utama**: Gemini 2.5 Flash / Pro.
- **Log Prompting Ringkas**:
  1. *"Bagaimana cara membuat fungsi helper di views.py untuk mengecek apakah user terdaftar dalam grup 'Editor' di Django?"*
  2. *"Bantu sesuaikan views.py dan urls.py untuk membatasi akses create, edit, dan delete experience serta project hanya untuk Superuser dan grup Editor."*
  3. *"Bagaimana cara menyembunyikan tombol Add, Edit, dan Delete di template HTML jika user bukan Superuser atau Editor?"*
  4. *"Bagaimana cara membatasi field yang di-serialize ke JSON pada Django serializers agar tidak membocorkan data User?"*

### Keterbatasan AI dan perbaikan manual yang saya lakukan

Meski AI sangat membantu dalam mempercepat penyusunan logika pengkondisian dan keamanan, tetap ada beberapa hal yang harus saya perbaiki dan sesuaikan sendiri secara manual:

1. **Penyesuaian Struktur Relasi Model pada `toggle_star`**:
   - **Masalah**: AI sempat menyarankan penggunaan relasi `starred_by` pada model `Project`, padahal nama atribut ManyToMany yang saya definisikan di model adalah `stars`.
   - **Perbaikan**: Saya memperbaikinya secara manual di fungsi `toggle_star` di `views.py` dengan menggunakan `project.stars.filter(...)` dan `project.stars.add/remove(...)` agar sesuai dengan skema model yang ada.

2. **Kesesuaian Jalur Tempat Berkas Template (Directory Structure)**:
   - **Masalah**: Saat AI memberikan contoh perintah Git untuk menyimpannya, AI mengasumsikan folder template berada di `main/templates/`, sementara pada proyek saya berkas template diletakkan di root folder `templates/`.
   - **Perbaikan**: Saya menyesuaikan lokasi path berkas secara manual saat menjalankan perintah `git add templates/` di terminal.

3. **Pembersihan Routing dan URL Duplikat**:
   - **Masalah**: Pada berkas `urls.py`, terdapat beberapa deklarasi path yang berulang (duplikat path `login/` dan `register/`).
   - **Perbaikan**: Saya merapikan isi `urls.py` secara manual dengan menghapus baris duplikat agar pemanggilan *named URL* berjalan bersih dan tanpa potensi bentrok routing.

### Tugas 5

1. *Debouncing* itu teknik buat menunda pemanggilan fungsi pencarian sampai pengguna benar-benar berhenti mengetik selama jeda waktu tertentu (misalnya 300 milidetik). Teknik ini penting banget di fitur pencarian AJAX karena kalau enggak pakai *debouncing*, browser bakal ngirim *request* ke server untuk setiap satu huruf yang kita ketik. Contohnya, kalau kita ngetik "Software", bakal ada 8 kali pemanggilan API ke server secara beruntun. Dengan *debouncing*, *request* baru dikirim 1 kali saja setelah kita selesai mengetik, jadi bisa menghemat *bandwidth*, meringankan beban server/database, dan bikin aplikasi terasa lebih cepat tanpa *lag*.

2. Fungsi utama atribut `await` saat memanggil `fetch()` adalah buat memberi tahu JavaScript supaya menunggu proses pengambilan data dari *network/server* selesai terlebih dahulu sebelum mengeksekusi baris kode berikutnya. Kalau kita enggak pakai `await` (dan juga enggak pakai `.then()`), `fetch()` cuma bakal mengembalikan objek *Promise* yang statusnya masih *pending*. Akibatnya, JavaScript langsung lanjut jalan ke baris bawahnya padahal datanya belum selesai dimuat, yang bikin kodenya *error* (`undefined`), gagal *render* komponen di DOM, atau nampilkan data kosong.

3. Serangan XSS (*Cross-Site Scripting*) adalah kerentanan keamanan web di mana penyerang berhasil memasukkan skrip JavaScript jahat ke dalam database atau input web yang kemudian tereksekusi di browser pengunjung lain. Data yang ditampilkan lewat AJAX/JavaScript jauh lebih rentan terhadap XSS dibanding template Django biasa karena saat kita menggunakan `.innerHTML` atau *template literals* di JavaScript, browser akan langsung menganggap string tersebut sebagai HTML mentah tanpa memfilter karakter berbahaya (seperti `<` atau `>`). Sementara di Django template biasa, Django punya fitur *auto-escaping* otomatis yang langsung mengubah tag berbahaya menjadi teks biasa sebelum di-render ke layar.

### Dokumentasi & AI Disclosure
Proyek pada Tugas 5 ini dikembangkan dengan memanfaatkan AI (Gemini) sebagai *collaborator*, *code reviewer*, serta alat *debugging* untuk fitur pencarian AJAX, modal popover, dan pengamanan XSS.

### Tools & Log Prompting
Tool Utama: Gemini 2.5 Flash / Pro.  
Log Prompting Ringkas:
1. "Bagaimana cara menerapkan fungsi search debouncing dengan delay 300ms di JavaScript untuk input pencarian AJAX?"
2. "Bantu periksa kenapa tombol Hapus dan Star di kartu proyek yang dibuat lewat JavaScript innerHTML mengalami error CSRF token."
3. "Bagaimana cara melakukan sanitasi input teks di Django Form menggunakan strip_tags untuk mencegah XSS?"

### Keterbatasan AI dan Perbaikan Manual yang Saya Lakukan

Walaupun AI sangat membantu mempercepat penulisan skrip AJAX dan pemecahan *error*, tetap ada beberapa kendala logika dan struktur kode yang harus saya perbaiki secara manual:

1. **Penyesuaian Nama Field Model (`thumbnail` vs `project_image_url`)**:
   * Masalah: AI sempat membuat skrip form modal dan fungsi JSON dengan nama field `project_image_url`, padahal di `models.py` dan `ProjectForm` milik saya nama field gambar yang digunakan adalah `thumbnail`.
   * Perbaikan: Saya mengedit ulang atribut `name="thumbnail"` pada input HTML di `project.html` dan menyesuaikan pemanggilan atribut di `views.py` agar data gambar tersimpan dengan benar ke database.

2. **Error Handling & Permission pada Endpoint AJAX (`create_project_ajax`)**:
   * Masalah: AI secara default hanya mengecek hak akses `is_superuser` di view AJAX, sehingga pengguna dengan grup *Editor* tidak bisa menambahkan data proyek atau pengalaman via modal.
   * Perbaikan: Saya memperbarui pemeriksaan *permission* di `views.py` menggunakan `if not (request.user.is_superuser or is_editor(request.user))` serta menyesuaikan penanganan pesan *error* JSON di skrip `fetch()` JavaScript.

3. **Perbaikan Mismatched Function Name (`show_project` vs `show_projects`)**:
   * Masalah: Terjadi `ImportError` saat menjalankan server karena adanya ketidakcocokan nama fungsi *view* antara `urls.py` dan `views.py`.
   * Perbaikan: Saya menyelaraskan nama fungsi di `views.py` menjadi `show_project` dan memperbaiki pengambilan relasi *stars* (`stars.all()`) menggunakan `list()` dan `len()` agar tidak memicu *500 Internal Server Error*.

### Tugas 6

1. **Apa itu REST dan Alasan Mengapa JSON Saja Belum Cukup Disebut RESTful, serta Perbedaan PUT vs PATCH:**
   * **Pengertian REST & RESTful**: REST (*Representational State Transfer*) adalah standar arsitektur komunikasi web yang memanfaatkan protokol HTTP secara *stateless* untuk mengelola sumber daya (*resource*). Mengembalikan format JSON saja **belum cukup** untuk membuat sebuah API disebut *RESTful*. Sebuah API baru bisa disebut *RESTful* jika mematuhi kendala arsitektural REST (*REST constraints*), seperti penggunaan *HTTP Method* yang tepat dan semantik (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), status kode HTTP yang sesuai (`200 OK`, `201 Created`, `400 Bad Request`, `403 Forbidden`, `404 Not Found`, `204 No Content`), bersifat *stateless*, serta menerapkan prinsip *HATEOAS* (Hypermedia as the Engine of Application State) di mana respons juga menyediakan tautan/navigasi ke aksi sumber daya terkait.
   * **Perbedaan PUT dan PATCH**:
     * **PUT**: Digunakan untuk mengganti/memperbarui *seluruh* data objek secara utuh (*full replacement*). Jika ada *field* yang tidak dikirim di dalam *payload* `PUT`, maka *field* tersebut akan di-reset atau dianggap kosong/null.
       * *Contoh*: Digunakan saat mengedit formulir data profil secara lengkap di mana semua kolom diisi ulang secara menyeluruh.
     * **PATCH**: Digunakan untuk memperbarui *sebagian* data saja (*partial update*). Hanya *field* yang dikirim di dalam *payload* yang akan diubah, sedangkan *field* lainnya di database tetap utuh tanpa terpengaruh.
       * *Contoh*: Digunakan saat men-toggle status *star* sebuah proyek atau mengedit judul pengalaman saja tanpa perlu mengirim ulang deskripsi dan tanggalnya.

2. **Peran Serializer di Django REST Framework (DRF) dan Keunggulannya dibanding JsonResponse Manual:**
   * **Peran Serializer**: Serializer berfungsi sebagai jembatan dua arah (penerjemah). Serializer mengubah objek kompleks Django ORM (*Model Instance*) menjadi tipe data Python *native* yang bisa dirender dengan mudah menjadi JSON (proses *serialization*). Selain itu, Serializer juga menerima data JSON dari request untuk divalidasi dan diubah kembali menjadi objek *Model Instance* yang siap disimpan ke database (proses *deserialization*).
   * **Keunggulan dibanding `JsonResponse` manual**:
     * **Validasi Otomatis & Terpusat**: DRF Serializer menangani validasi tipe data, pemeriksaan field wajib, sanitasi teks (`strip_tags`), hingga *custom validation* (`validate_<field>`) secara otomatis. Jika data invalid, Serializer langsung menghasilkan struktur error yang rapi dengan HTTP status `400 Bad Request`.
     * **Manajemen Field Read-Only & Calculated Fields**: Kita bisa menambahkan field hasil perhitungan (*computed fields* seperti `star_count` atau `is_starred`) dan menjamin field sensitif/internal tidak bisa dimanipulasi oleh user karena diset sebagai `read_only_fields`.
     * **Kode Lebih Bersih & DRY**: Nggak perlu lagi nulis perulangan dictionary manual satu per satu seperti di `JsonResponse(list(data.values()))`. Cukup panggil `Serializer(data, many=True).data`.

3. **Perbedaan Autentikasi vs Otorisasi dan Alasan Pentingnya Permission Class di Server:**
   * **Autentikasi vs Otorisasi**: 
     * **Autentikasi (*Who are you?*)**: Proses untuk mengonfirmasi identitas pengguna (misalnya mengecek username/password atau session cookie saat pengguna login).
     * **Otorisasi (*What can you do?*)**: Proses mengecek apakah pengguna yang sudah terautentikasi tersebut memiliki izin/hak akses untuk melakukan tindakan tertentu pada suatu sumber daya.
   * **Alasan Harus Diperiksa di Server (*Permission Class*)**: Menyembunyikan tombol Edit/Delete di template HTML cuma proteksi visual di tingkat tampilan (*User Interface*). Pengunjung nakal atau *attacker* masih bisa menembak *endpoint* API backend secara langsung memakai tools seperti `curl`, Postman, atau Fetch API lewat konsol browser. Jika server tidak diproteksi dengan `permission_classes`, backend akan tetap memproses permintaan destruktif tersebut. Oleh karena itu, pemeriksaan hak akses wajib dieksekusi di level server backend.

4. **Kebutuhan Token CSRF pada SessionAuthentication dan Keterbatasan `force_authenticate` dalam Testing:**
   * **Mengapa Tetap Butuh Token CSRF di SessionAuthentication**: `SessionAuthentication` mengandalkan cookie sesi yang disimpan oleh browser. Browser secara otomatis menyertakan cookie sesi ini pada setiap permintaan HTTP yang dikirimkan ke domain server kita, termasuk jika permintaan tersebut dipicu secara tersembunyi oleh situs web lain yang berbahaya (*Cross-Site Request Forgery* / CSRF). Token CSRF berfungsi sebagai rahasia acak tambahan yang wajib dikirimkan di header HTTP (`X-CSRFToken`) untuk membuktikan bahwa permintaan perubahan data benar-benar dipicu oleh antarmuka web kita yang sah, bukan jebakan situs eksternal.
   * **Keterbatasan `force_authenticate`**: Metode `force_authenticate` pada DRF `APITestCase` bekerja dengan cara menyuntikkan (*inject*) objek `user` langsung ke dalam instance `request` tanpa melewati alur autentikasi berbasis *session* dan tanpa memicu *middleware* CSRF Django. Karena *middleware* CSRF dilewati saat `force_authenticate` dipakai, tes tidak bisa membuktikan apakah proteksi CSRF bekerja dengan baik. Untuk membuktikannya, kita wajib menggunakan `APIClient(enforce_csrf_checks=True)` yang dikombinasikan dengan `.login()`.

### Dokumentasi & AI Disclosure
Pada pengerjaan Tugas 6 ini, saya kembali menggunakan AI (Gemini) sebagai *pair-programmer*, panduan penyusunan DRF Serializer & Permissions, serta alat *debugging* saat menghadapi kendala integrasi AJAX dan penyesuaian tes API.

### Tools & Log Prompting
* **Tool Utama**: Gemini 2.5 Flash / Pro.
* **Log Prompting Ringkas**:
  1. *"Bagaimana cara menyesuaikan IsPortfolioOwnerOrReadOnly di DRF agar mengizinkan grup Editor melakukan aksi PUT dan PATCH tetapi melarang POST dan DELETE?"*
  2. *"Bantu selesaikan error NoReverseMatch pada APITestCase untuk model Experience yang menggunakan UUID sebagai primary key."*
  3. *"Bagaimana cara menangani permintaan fetch() AJAX di frontend experience.html agar mengirimkan header X-CSRFToken dan menampilkan toast error saat API mengembalikan HTTP status 400 atau 403?"*

### Keterbatasan AI dan Perbaikan Manual yang Saya Lakukan

Walaupun AI sangat membantu mempercepat penulisan skrip serializer dan penyusunan fungsi API views DRF, tetap ada beberapa kendala struktur yang harus saya perbaiki secara manual:

1. **Penyesuaian Path Converter UUID pada `api_urls.py`**:
   * **Masalah**: AI sempat menyarankan konverter URL standar `<int:pk>` untuk rute detail `Experience`. Hal ini menyebabkan error `NoReverseMatch` saat tes dijalankan karena model `Experience` di proyek saya menggunakan tipe data `UUIDField`.
   * **Perbaikan**: Saya memperbaikinya secara manual pada berkas `api_urls.py` dengan mengubah pola path converter menjadi `<uuid:pk>` agar pas dengan tipe data primary key `Experience`.

2. **Pemisahan Permission Class antara Projects dan Experience**:
   * **Masalah**: Ketika saya mengubah logika `IsPortfolioOwnerOrReadOnly` agar Editor dapat melakukan `PUT`/`PATCH` pada Experience, tes bawaan Tutorial 07 untuk `Project` mengalami kegagalan (*assertion error 403 != 200*) karena tes tutorial mewajibkan Editor ditolak saat mengedit proyek tutorial.
   * **Perbaikan**: Saya memisahkan permission class di `main/permissions.py` secara manual dengan membuat `IsExperienceOwnerOrEditorOrReadOnly` khusus untuk fitur Experience, sehingga aturan baru bagi Editor berjalan sempurna di Experience tanpa merusak integritas tes Tutorial 07.

3. **Perbaikan Format Dummy ID pada JavaScript Template (`experience.html`)**:
   * **Masalah**: Kode JavaScript yang dihasilkan AI menggunakan angka `0` sebagai *placeholder* reverse URL Django (`reverse("api:experience-detail", args=[0])`), yang memicu error saat rendering template karena Django menolak angka `0` untuk rute berbasis UUID.
   * **Perbaikan**: Saya mengganti *placeholder* reverse URL di `experience.html` secara manual menggunakan string dummy UUID valid `'00000000-0000-0000-0000-000000000000'`, lalu me-replace string tersebut secara dinamis dengan ID pengalaman riil saat request *fetch* dijalankan.