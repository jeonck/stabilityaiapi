import requests
import json

url = "https://stablediffusionapi.com/api/v1/enterprise/get_all_models"

payload = json.dumps({
 "key": "ㅇㅇㅇ"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)