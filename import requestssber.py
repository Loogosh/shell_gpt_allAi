import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2"

payload={
  'scope': 'GIGACHAT_API_PERS'
}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': '7f7cc971-38a8-4636-98e6-4357a63dc2a6',
  'Authorization': 'Base NDE3NjU0MTItZWYyMC00MjI5LWE0YTAtYTIxNTVjMDRlZDI4OmUwZGUwMWMwLTg5ZWYtNGY1Ni04MDg4LTA5MmJkZWMxNGU4Yg=='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)