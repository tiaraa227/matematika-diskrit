python = {"Fia", "Gevano", "Ara"}
java = {"Gevano", "Langit"}
sql = {"Fia", "Langit", "Eka"}
semua_mahasiswa = {"Fia", "Gevano", "Ara", "Langit", "Eka", "Haikal"}

python_saja = python - (java | sql)
python_dan_java = python & java
minimal_satu = python | java | sql
tidak_menyukai_ketiganya = semua_mahasiswa - (python | java | sql)

print("Python saja:", python_saja)
print("Python dan Java:", python_dan_java)
print("Minimal satu teknologi:", minimal_satu)
print("Tidak menyukai ketiganya:", tidak_menyukai_ketiganya)