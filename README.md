### MEMBUAT PERSONAL PORTFOLIO WEBSITE
https://github.com/gurnitha/django-personal-portfolio-website


### 1. PRASYARAT
----------------

        1. Menginstal Python versi 3+ 
        2. Menginstal Pip
        3. Memastikan Python dan Pip sudah terinstal
        4. Menginstal Text Editor
        5. Menginstal Terminal



### 2. INISIAL SETUP
--------------------

        1. Membuat root folder 'personal-portfolio-website'
        2. cd personal-portfolio-website
        3. Membuat README.md file
        4. Membuat .gitignore file
        5. Mengisi nama-nama file yg akan di-ignore oleh Git
           pada .gitignore file
        6. Memeriksa hasilnya



### 3. MEMBUAT LOKAL DAN REMOTE REPOSITORI
------------------------------------------

#### 3.1 Menyimpan inisiasi proyek pada lokal repositori

        Steps:

        1. git init
        2. git add .
        3. git status
        4. git add .
        5. git commit -m "message"

        new file:   .gitignore
        new file:   README.md


#### 3.2 Membuat remote repository pada Github dan men-deploy file proyek ke remote repositori tersebut.

        Steps:

        1. Membuat remote repositori
        2. Mendeploy file proyek ke remote repositori
        3. Memeriksa hasilnya

        https://github.com/gurnitha/django-personal-portfolio-website 

        modified:   README.md



### 4. PROYEK PROTOTYPE
-----------------------

#### 4.1 Demo proyek prototype

        modified:   README.md



### 5. MEMBUAT DJANGO PROYEK DAN APP
------------------------------------

#### 5.1 Membuat django proyek dengan nama 'config'

        Steps:

        1. Membuat virtual environment 'venv39326'
        2. Mengaktifkan venv39326
        3. Menginstal Django Framework versi 3.2.6
        4. Meng-upgrade pip
        5. Menginstal Django Rest Framework
        6. Membuat django proyek 'config'
        7. Jalankan server untuk menguji hasilnya

        modified:   .gitignore
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 5.2 Install django Rest Framework

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py


#### 5.3 Membuat django app 'apps/user_interface'

        Steps:

        1. Membuat folder baru 'apps'
        2. Membuat folder baru 'apps/user_interface'
        3. Membuat django app 'apps/user_interface'
        4. Modifikasi file user_interface/apps.py
        5. Instal 'user_interface' app pada config/settings.py
        6. Jalankan server untuk menguji

        modified:   README.md
        new file:   apps/user_interface/__init__.py
        new file:   apps/user_interface/admin.py
        new file:   apps/user_interface/apps.py
        new file:   apps/user_interface/migrations/__init__.py
        new file:   apps/user_interface/models.py
        new file:   apps/user_interface/tests.py
        new file:   apps/user_interface/views.py
        modified:   config/settings.py



### 6. MEMBUAT HELLO WORLD DENGAN UVT


#### 6.1 Membuat Hello World dengn Urls, View dan HttpResponse

        modified:   README.md
        new file:   apps/user_interface/urls.py
        modified:   apps/user_interface/views.py
        modified:   config/urls.py

        Steps:

        1. Membuat urls
        2. Membuat views
        3. Meng-include urls pada proyek
        4. Memastikan hasilnya



### 7. DJANGO MODEL


#### 7.1 Membuat User model Menggunakan AbstractUser

        Steps:

        1. Import AbstractUser
        2. Membuat User model
        3. Memeriksa hasilnya
        4. Solusinya
        5. Memeriksa hasilnya

        modified:   README.md
        new file:   apps/user_interface/migrations/0001_initial.py
        modified:   apps/user_interface/models.py
        modified:   config/settings.py


#### 7.2 Membuat Information model

        Steps:

        1. Membuat model
        2. Jalankan migrasi
        3. Periksa hasilnya
        
        modified:   README.md
        new file:   apps/user_interface/migrations/0002_informationmodel.py
        modified:   apps/user_interface/models.py