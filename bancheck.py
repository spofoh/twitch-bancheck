import requests
import json

# Benutzername vom Benutzer abfragen
username = input("Please enter the username: ")

url = "https://gql.twitch.tv/gql"

# Benutzername in der Anfrage verwenden
payload = f"[{{\"operationName\":\"ChannelShell\",\"variables\":{{\"login\":\"{username}\"}},\"extensions\":{{\"persistedQuery\":{{\"version\":1,\"sha256Hash\":\"580ab410bcd0c1ad194224957ae2241e5d252b2c5173d8e0cce9d32d5bb14efe\"}}}}}}]"
headers = {
  'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko'
}

response = requests.request("POST", url, headers=headers, data=payload)

with open('response.json', 'w') as f:
    json.dump(response.json(), f)

print("The answer has been saved in the file response.json.")
