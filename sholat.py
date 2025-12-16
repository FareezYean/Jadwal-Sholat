import requests
data_url= "https://api.aladhan.com/v1/timingsByCity/09-12-2025?city=Jakarta&country=Indonesia&method=20"
response = requests.get(data_url)
data = response.json()
jadwal_sholat = data['data']['timings']

print(data['data']['timings']['Fajr'])

shubuh = jadwal_sholat['Fajr']
dzuhur = jadwal_sholat['Dhuhr']
ashar = jadwal_sholat['Asr']
maghrib = jadwal_sholat['Maghrib']
isya = jadwal_sholat['Isha']
