import requests

city = input("Masukkan nama kota: ")

if not city.isalpha():
    print("Error: Nama kota harus berupa huruf saja!")
    exit()

print("\nMenu:")
print("1. Jadwal hari ini")
print("2. Jadwal besok")

Pilih = input("Pilih (1/2): ")

if Pilih == "1":
    offset = 0
elif Pilih == "2":
    offset = 1
else:
    print("Pilihan tidak valid")
    exit()

url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Indonesia&method=20&offset={offset}"
response = requests.get(url)
data = response.json()

timings = data["data"]["timings"]
hijri = data["data"]["date"]["hijri"]["date"]

print("\n===========================")
print(f"Jadwal Sholat Kota {city}")
print(f"Tanggal Hijriah: {hijri}")
print("===========================")
print("Subuh   :", timings["Fajr"])
print("Dzuhur  :", timings["Dhuhr"])
print("Ashar   :", timings["Asr"])
print("Maghrib :", timings["Maghrib"])
print("Isya    :", timings["Isha"])
print("===========================")
