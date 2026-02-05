import requests

URL = "https://it-tr-appointment.idata.com.tr/tr/membership/login"

response = requests.get(URL, timeout=20)

print("Status code:", response.status_code)

with open("last_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML kaydedildi (last_page.html)")
