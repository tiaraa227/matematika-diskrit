nama = "Sari"       # str
umur = 19            # int
ipk = 3.75           # float
mahasiswa_aktif = True  # bool

print(nama, umur, ipk, mahasiswa_aktif)

# Daftar data mahasiswa pendaftar beasiswa
mahasiswa = [
    {"nama": "Rian", "status_aktif": True, "ipk": 3.7, "semester": 5, "cuti": False, "organisasi": {"Hima", "BEM"}},
    {"nama": "Siti", "status_aktif": True, "ipk": 3.2, "semester": 3, "cuti": False, "organisasi": {"Hima"}},
    {"nama": "Bayu", "status_aktif": False, "ipk": 3.8, "semester": 5, "cuti": True, "organisasi": {"BEM"}},
    {"nama": "Dewi", "status_aktif": True, "ipk": 3.5, "semester": 7, "cuti": False, "organisasi": {"Fuki", "Hima"}},
]

def seleksi_beasiswa(data):
    return (
        data["status_aktif"]                  # Syarat 1: Harus aktif kuliah
        and data["ipk"] >= 3.4                # Syarat 2: IPK minimal 3.4
        and data["semester"] >= 4             # Syarat 3: Minimal berada di semester 4
        and not data["cuti"]                  # Syarat 4: Tidak sedang mengambil cuti
        and bool(data["organisasi"] & {"Hima", "BEM"}) # Syarat 5: Wajib ikut salah satu organisasi (Hima atau BEM)
    )

# Mengecek dan mencetak hasil seleksi
for data in mahasiswa:
    status_hasil = "diterima" if seleksi_beasiswa(data) else "tidak diterima"
    print(data["nama"], "->", status_hasil)


    peserta = [
    {"nama": "Ani", "aktif": True, "nilai": 80, "kehadiran": 90,
     "sanksi": False, "teknologi": {"Python"}},
    {"nama": "Budi", "aktif": True, "nilai": 59, "kehadiran": 88,
     "sanksi": False, "teknologi": {"SQL"}},
    {"nama": "Citra", "aktif": True, "nilai": 75, "kehadiran": 75,
     "sanksi": False, "teknologi": {"Java"}},
    {"nama": "Deni", "aktif": False, "nilai": 90, "kehadiran": 95,
     "sanksi": False, "teknologi": {"Python", "SQL"}},
]

def lolos(data):
    return (
        data["aktif"]
        and data["nilai"] >= 60
        and data["kehadiran"] >= 75
        and not data["sanksi"]
        and bool(data["teknologi"] & {"Python", "SQL"})
    )

for data in peserta:
    print(data["nama"], "lolos" if lolos(data) else "tidak lolos")