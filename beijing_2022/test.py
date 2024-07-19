import requests
import json

url = "http://59.110.169.173:5000/api/group"

payload = {
    "main_zd": "Z51.103",
    "other_zd": "",
    "main_ss": "99.2503",
    "other_ss": "",
    "gender": "2",
    "dept": "0302",
    "inHospitalTime": 14,
    "leavingType": "1",
    "age": 10,
    "age_days": 21,
    "weight": 3200
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    print("Response JSON:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
